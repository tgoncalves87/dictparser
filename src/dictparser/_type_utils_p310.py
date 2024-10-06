# pylint: disable=R0801
import typing
import types


__all__ = ['_get_origin', '_is_union_type', '_get_args']


def _get_origin(t):
    return typing.get_origin(t)


def _is_union_type(t):
    origin = _get_origin(t)
    return origin in (types.UnionType, typing.Union)


def _get_args(t):
    return list(typing.get_args(t))
