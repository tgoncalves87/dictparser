import abc
import collections.abc
import pathlib
import dataclasses
import typing
import os
import yaml

from ._dictparser_data import CLASS_DATA_FIELD_NAME
from ._type_utils import type_get_origin, type_get_args, is_union_type, strip_generic_from_type


_in_test = os.environ.get('PYTEST_VERSION') is not None


class Converter(abc.ABC):
    def __init__(self, mapper, res_types):
        self.mapper = mapper
        self.res_types = res_types

    def from_dict(self, data):
        if self.mapper.check_res_types:
            res = self.convert_value(data)
            self._validate_res_type(res)
            return res
        else:
            return self.convert_value(data)

    @abc.abstractmethod
    def convert_value(self, data):
        pass

    def _validate_res_type(self, res):
        for i in self.res_types:
            if isinstance(res, i):
                return

        raise RuntimeError(f"Converted value does not match expected result type: {type(res)} vs {self.res_types}")


class Mapper:
    def __init__(self):
        self.check_res_types = _in_test
        self._converters = {}

    def from_dict(self, cls, data):
        converter = self.get_converter_for_type(cls)
        return converter.from_dict(data)

    def from_file(self, cls, file):
        with open(file, "rt", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return cls.from_dict(data)

    def as_dict(self, value):
        return dataclasses.asdict(value)

    def get_converter_for_type(self, vtype):
        converter = self._converters.get(vtype, None)
        if converter is not None:
            return converter

        self._converters[vtype] = self._init_converter_for_type(vtype)
        return self._converters[vtype]

    def _init_converter_for_type(self, vtype) -> Converter:  # pylint: disable=too-many-return-statements,too-many-branches
        if vtype is type(None) or vtype is None:
            return NullConverter(self)

        if vtype in (bool, int, float, complex, str, bytes, bytearray, pathlib.Path):
            return ConstructorConverter(self, vtype)

        if hasattr(vtype, CLASS_DATA_FIELD_NAME):
            return DictparserConverter(self, vtype)

        if hasattr(vtype, "from_dict"):
            return FromDictConverter(self, vtype)

        vtype_origin = type_get_origin(vtype)
        if vtype_origin is not None:
            if is_union_type(vtype):
                args = type_get_args(vtype)

                if len(args) == 1:
                    return self._init_converter_for_type(args[0])

                has_null = False
                others = []
                for a in args:
                    if a is type(None) or a is None:
                        has_null = True
                    else:
                        others.append(a)

                if has_null and len(others) == 1:
                    return OptionalConverter(self, [type(None), strip_generic_from_type(others[0])], others[0])

                raise NotImplementedError(f"Union type {vtype} with <> 2 arguments is not supported")

            elif vtype_origin in (list, typing.List):
                args = type_get_args(vtype)

                if len(args) != 1:
                    raise RuntimeError("List type annotation has an amount of argument types different than 1")

                return ListConverter(self, [list], args[0])

            elif vtype_origin in (dict, typing.Dict):
                args = type_get_args(vtype)

                if len(args) != 2:
                    raise RuntimeError("Dict type annotation has an amount of argument types different than 2")

                return DictConverter(self, [dict], args[0], args[1])

            #elif origin in (tuple, ): This is alot more complicated than this
            #    args = _get_args(field_type)
            #    return ListTypeData(field_type, [tuple], parse_field_type(args[0]))

            else:
                raise NotImplementedError(f"'origin {vtype_origin}' not implemented")

        raise NotImplementedError(f"{vtype}")


class NullConverter(Converter):
    def __init__(self, mapper):
        super().__init__(mapper, [type(None)])

    def convert_value(self, data):
        if data is None:
            return None

        raise RuntimeError(f"Invalid data type '{type(data)}' for field type of None")


class ConstructorConverter(Converter):
    def __init__(self, mapper, vtype):
        super().__init__(mapper, [vtype])
        self.vtype = vtype

    def convert_value(self, data):
        if isinstance(data, self.vtype):
            return data

        return self.vtype(data)


class DictparserConverter(Converter):
    def __init__(self, mapper, cls_type):
        super().__init__(mapper, [cls_type])
        self.cls_type = cls_type

    def convert_value(self, data):
        if isinstance(data, self.cls_type):
            return data

        class_data = getattr(self.cls_type, CLASS_DATA_FIELD_NAME)

        if not isinstance(data, collections.abc.Mapping):
            raise RuntimeError("data is not a dict like value")

        args = {}
        keys = set(data.keys())

        for field in class_data.fields.values():
            if field.data_key in data:
                converter = self.mapper.get_converter_for_type(field.field_type)
                args[field.field_name] = converter.from_dict(data[field.data_key])
                keys.remove(field.data_key)
            elif field.has_default:
                args[field.field_name] = field.get_default_value()
            elif field.required:
                raise RuntimeError(f"Required field '{field.field_name}' is missing")
            else:
                raise RuntimeError("ups")

        if len(keys) > 0 and not class_data.ignore_extra:
            raise RuntimeError(f"Extra data keys: {list(keys)}")

        return class_data.result_cls(**args)


class FromDictConverter(Converter):
    def __init__(self, mapper, cls_type):
        super().__init__(mapper, [cls_type])
        self.cls_type = cls_type

    def convert_value(self, data):
        if isinstance(data, self.cls_type):
            return data

        return getattr(self.cls_type, "from_dict")(data)


class ListConverter(Converter):
    def __init__(self, mapper, res_types, item_type):
        super().__init__(mapper, res_types)
        self.item_type = item_type

    def convert_value(self, data):
        converter = self.mapper.get_converter_for_type(self.item_type)
        return self.res_types[0](
            [converter.convert_value(v) for v in data]
        )


class DictConverter(Converter):
    def __init__(self, mapper, res_types, key_type, value_type):
        super().__init__(mapper, res_types)
        self.key_type = key_type
        self.value_type = value_type

    def convert_value(self, data):
        key_converter = self.mapper.get_converter_for_type(self.key_type)
        value_converter = self.mapper.get_converter_for_type(self.value_type)
        return self.res_types[0](
            [(key_converter.convert_value(k), value_converter.convert_value(v)) for k, v in data.items()]
        )


class OptionalConverter(Converter):
    def __init__(self, field_type, res_types, item_type):
        super().__init__(field_type, res_types)
        self.item_type = item_type

    def convert_value(self, data):
        if data is None:
            converter = self.mapper.get_converter_for_type(None)
        else:
            converter = self.mapper.get_converter_for_type(self.item_type)

        return converter.convert_value(data)
