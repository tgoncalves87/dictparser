# pylint: disable=R0801
import typing


__all__ = ['_get_origin', '_is_union_type', '_get_args']


def _get_origin(t):
    if hasattr(t, "__origin__"):
        return t.__origin__
    else:
        return None


def _is_union_type(t):
    origin = _get_origin(t)
    return origin in (typing.Union, )


def _get_args(t):
    return list(t.__args__)
