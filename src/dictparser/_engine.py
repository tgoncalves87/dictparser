import copy
import dataclasses

from .mapper import Mapper
from ._dictparser_data import CLASS_DATA_FIELD_NAME, MISSING, ClassData, Field
from ._type_utils import setattr_method, setattr_classmethod


_default_mapper = Mapper()


def process_class(cls, kw_only):
    fields = {}

    for base in cls.__mro__[-1:0:-1]:
        base_data = getattr(base, CLASS_DATA_FIELD_NAME, None)
        if base_data is not None:
            for field in base_data.fields.values():
                fields[field.field_name] = field

    if hasattr(cls, "__annotations__"):
        for field_name, field_type in cls.__annotations__.items():
            default = MISSING
            default_factory = MISSING

            if hasattr(cls, field_name):
                default = getattr(cls, field_name)
                delattr(cls, field_name)

            if default is not MISSING:
                default = _default_mapper.get_converter_for_type(field_type).convert_value(default)

                if default.__class__.__hash__ is None:
                    def copy_factory(default):
                        return lambda : copy.deepcopy(default)

                    default_factory = copy_factory(default)
                    default = MISSING

            fields[field_name] = Field(field_name, field_type, field_name, default, default_factory)

    #
    #
    #
    _class_data = ClassData()
    setattr(cls, CLASS_DATA_FIELD_NAME, _class_data)

    _class_data.fields = fields

    for field in _class_data.fields.values():
        if not field.has_default:
            _class_data.has_required = True
            break

    _class_data.result_cls = cls

    #
    #
    #
    setattr_classmethod(cls, "from_dict", from_dict)
    setattr_classmethod(cls, "from_file", from_file)
    setattr_method(cls, "as_dict", as_dict)

    return dataclasses.dataclass(cls)


def from_dict(cls, data):
    return _default_mapper.from_dict(cls, data)


def from_file(cls, file):
    return _default_mapper.from_file(cls, file)


def as_dict(value):
    return _default_mapper.as_dict(value)


def get_fields(class_or_instance):
    data = getattr(class_or_instance, CLASS_DATA_FIELD_NAME, None)
    if data is None:
        raise TypeError("Value needs to be a class created by dictparser or be an instance of such a class")

    return tuple(data.fields.values())
