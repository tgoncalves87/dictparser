import pytest

from dictparser import dictparser, type_info, from_dict, to_dict


@type_info(data_key="type")
@dictparser()
class Base:
    common: int = 1


@type_info(name='A1')
@dictparser()
class A1(Base):
    a: str = "a1"


@type_info(name='A2')
@dictparser()
class A2(A1):
    a: str = "a2"


@type_info(name='B1')
@dictparser()
class B1(Base):
    b: str = "b1"


@type_info(name='B2')
@dictparser()
class B2(B1):
    b: str = "b2"


@pytest.mark.parametrize("cls,data,expected", [
    (Base, {"type": "A1"}, A1(1, "a1")),
    (A1,   {"type": "A1"}, A1(1, "a1")),
    (A2,   {"type": "A1"}, None),
    (B1,   {"type": "A1"}, None),
    (B2,   {"type": "A1"}, None),
    (Base, {"type": "A2"}, A2(1, "a2")),
    (A1,   {"type": "A2"}, A2(1, "a2")),
    (A2,   {"type": "A2"}, A2(1, "a2")),
    (B1,   {"type": "A2"}, None),
    (B2,   {"type": "A2"}, None),
    (Base, {"type": "B1"}, B1(1, "b1")),
    (A1,   {"type": "B1"}, None),
    (A2,   {"type": "B1"}, None),
    (B1,   {"type": "B1"}, B1(1, "b1")),
    (B2,   {"type": "B1"}, None),
    (Base, {"type": "B2"}, B2(1, "b2")),
    (A1,   {"type": "B2"}, None),
    (A2,   {"type": "B2"}, None),
    (B1,   {"type": "B2"}, B2(1, "b2")),
    (B2,   {"type": "B2"}, B2(1, "b2")),
])
def test_from_dict(cls, data, expected):
    if expected is not None:
        assert from_dict(cls, data) == expected
    else:
        with pytest.raises(Exception):
            from_dict(cls, data)


def test_to_dict():
    assert to_dict(A1(1, "a1")) == {"type": "A1", "common": 1, "a": "a1"}
    assert to_dict(A2(1, "a2")) == {"type": "A2", "common": 1, "a": "a2"}
    assert to_dict(B1(1, "b1")) == {"type": "B1", "common": 1, "b": "b1"}
    assert to_dict(B2(1, "b2")) == {"type": "B2", "common": 1, "b": "b2"}
