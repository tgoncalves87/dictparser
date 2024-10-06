from typing import Union, Optional, List, Dict
from dictparser import dictparser


@dictparser(kw_only=True)
class TopLevel:
    a1: Optional[bool]
    a2: Optional[bool]
    a3: Optional[bool] = True
    b1: Optional[int]
    b2: Optional[int]
    b3: Optional[int] = 3
    c1: Optional[str]
    c2: Optional[str]
    c3: Optional[str] = "default"
    d1: Optional[List[int]]
    d2: Optional[List[int]]
    d3: Optional[List[int]] = [1, 2, 3]
    e1: Optional[Dict[str, int]]
    e2: Optional[Dict[str, int]]
    e3: Optional[Dict[str, int]] = {"e3": 3}
    fa1: Union[bool, None]
    fa2: Union[bool, None]
    fa3: Union[bool, None] = True
    fb1: Union[None, bool]
    fb2: Union[None, bool]
    fb3: Union[None, bool] = True

    @classmethod
    def get_construct_data(cls):
        return {
            "a1": None,
            "a2": False,
            "b1": None,
            "b2": 2,
            "c1": None,
            "c2": "c2",
            "d1": None,
            "d2": [4, 5, 6],
            "e1": None,
            "e2": {"e2": 2},
            "fa1": None,
            "fa2": False,
            "fb1": None,
            "fb2": False,
        }

    def assert_defaults(self):  # pylint: disable=too-many-statements
        assert self.a1 is None
        assert self.a2 is False
        assert self.a3 is True
        assert self.b1 is None
        assert self.b2 == 2
        assert self.b3 == 3
        assert self.c1 is None
        assert self.c2 == "c2"
        assert self.c3 == "default"
        assert self.d1 is None
        assert self.d2 == [4, 5, 6]
        assert self.d3 == [1, 2, 3]
        assert self.e1 is None
        assert self.e2 == {"e2": 2}
        assert self.e3 == {"e3": 3}
        assert self.fa1 is None
        assert self.fa2 is False
        assert self.fa3 is True
        assert self.fb1 is None
        assert self.fb2 is False
        assert self.fb3 is True

def test_unions():
    """Tests @dictparser class construction from empty dict"""
    v = TopLevel.from_dict(TopLevel.get_construct_data())
    v.assert_defaults()
