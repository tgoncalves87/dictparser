# pylint: disable=R0801
from typing import Type, TypeVar, dataclass_transform

from .engine import process_class as _process_class
from .engine import from_dict as _from_dict
from .engine import from_file as _from_file
from .engine import as_dict as _as_dict
from .engine import get_fields as _get_fields


T = TypeVar("T")


@dataclass_transform()
def dictparser(cls: Type[T] | None=None, *, kw_only=False):
    def wrap(cls) -> Type[T]:
        return _process_class(cls, kw_only) # type: ignore

    if cls is None:
        return wrap

    return wrap(cls)


def from_dict(cls: Type[T], data) -> T:
    return _from_dict(cls, data)


def from_file(cls, file):
    return _from_file(cls, file)


def as_dict(value):
    return _as_dict(value)


def fields(class_or_instance):
    return _get_fields(class_or_instance)
