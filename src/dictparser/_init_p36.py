# pylint: disable=R0801
from ._engine import process_class as _process_class
from ._engine import from_dict as _from_dict
from ._engine import from_file as _from_file
from ._engine import as_dict as _as_dict
from ._engine import get_fields as _get_fields


def dictparser(cls=None, *, kw_only=False):
    def wrap(cls):
        return _process_class(cls, kw_only)

    if cls is None:
        return wrap

    return wrap(cls)


def from_dict(cls, data):
    return _from_dict(cls, data)


def from_file(cls, file):
    return _from_file(cls, file)


def as_dict(value):
    return _as_dict(value)


def fields(class_or_instance):
    return _get_fields(class_or_instance)
