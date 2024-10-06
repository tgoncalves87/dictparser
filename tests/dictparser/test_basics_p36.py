# pylint: disable=R0801
import sys

from typing import Optional, List, Dict
from dictparser import dictparser, from_dict, as_dict


if sys.version_info >= (3, 6):
    @dictparser
    class ClassABase:
        enable: bool


    @dictparser
    class ClassA(ClassABase):
        extra: bool


    @dictparser(kw_only=True)
    class TopLevel:
        a1: None
        a2: None = None
        b1: bool
        b2: bool = True
        b3: Optional[bool]
        b4: Optional[bool]
        b5: Optional[bool] = True
        b6: Optional[bool] = None
        c1: int
        c2: int = 1
        c3: Optional[int]
        c4: Optional[int]
        c5: Optional[int] = 2
        c6: Optional[int] = None
        d1: str
        d2: str = "default"
        d3: Optional[str]
        d4: Optional[str]
        d5: Optional[str] = "default"
        d6: Optional[str] = None
        e1: List[int]
        e2: List[int] = [1, 2, 3]
        e3: Optional[List[int]]
        e4: Optional[List[int]]
        e5: Optional[List[int]] = [1, 2, 3]
        e6: Optional[List[int]] = None
        f1: Dict[str, int]
        f2: Dict[str, int] = {"a": 1}
        f3: Optional[Dict[str, int]]
        f4: Optional[Dict[str, int]]
        f5: Optional[Dict[str, int]] = {"b": 2}
        f6: Optional[Dict[str, int]] = None
        g1: ClassA
        g2: ClassA = ClassA(True, True)
        g3: Optional[ClassA]
        g4: Optional[ClassA]
        g5: Optional[ClassA] = ClassA(True, True)
        g6: Optional[ClassA] = None
        h1: List[ClassA]
        h2: List[ClassA] = [ClassA(True, True)]
        h3: Optional[List[ClassA]]
        h4: Optional[List[ClassA]]
        h5: Optional[List[ClassA]] = [ClassA(True, True)]
        h6: Optional[List[ClassA]] = None
        i1: Dict[str, ClassA]
        i2: Dict[str, ClassA] = {"a": ClassA(True, True)}
        i3: Optional[Dict[str, ClassA]]
        i4: Optional[Dict[str, ClassA]]
        i5: Optional[Dict[str, ClassA]] = {"b": ClassA(True, True)}
        i6: Optional[Dict[str, ClassA]] = None

        @classmethod
        def get_construct_data(cls):
            return {
                "a1": None,
                "b1": False,
                "b3": False,
                "b4": None,
                "c1": 3,
                "c3": 4,
                "c4": None,
                "d1": "a",
                "d3": "b",
                "d4": None,
                "e1": [4, 5, 6],
                "e3": [4, 5, 6],
                "e4": None,
                "f1": {"c": 3},
                "f3": {"d": 4},
                "f4": None,
                "g1": {"enable": False, "extra": False},
                "g3": {"enable": False, "extra": False},
                "g4": None,
                "h1": [{"enable": False, "extra": False}],
                "h3": [{"enable": False, "extra": False}],
                "h4": None,
                "i1": {"c": {"enable": False, "extra": False}},
                "i3": {"d": {"enable": False, "extra": False}},
                "i4": None,
            }

        def assert_defaults(self):  # pylint: disable=too-many-statements
            assert self.a1 is None
            assert self.a2 is None
            assert self.b1 is False
            assert self.b2 is True
            assert self.b3 is False
            assert self.b4 is None
            assert self.b5 is True
            assert self.b6 is None
            assert self.c1 == 3
            assert self.c2 == 1
            assert self.c3 == 4
            assert self.c4 is None
            assert self.c5 == 2
            assert self.c6 is None
            assert self.d1 == "a"
            assert self.d2 == "default"
            assert self.d3 == "b"
            assert self.d4 is None
            assert self.d5 == "default"
            assert self.d6 is None
            assert self.e1 == [4, 5, 6]
            assert self.e2 == [1, 2, 3]
            assert self.e3 == [4, 5, 6]
            assert self.e4 is None
            assert self.e5 == [1, 2, 3]
            assert self.e6 is None
            assert self.f1 == {"c": 3}
            assert self.f2 == {"a": 1}
            assert self.f3 == {"d": 4}
            assert self.f4 is None
            assert self.f5 == {"b": 2}
            assert self.f6 is None
            assert self.g1 == ClassA(False, False)
            assert self.g2 == ClassA(True, True)
            assert self.g3 == ClassA(False, False)
            assert self.g4 is None
            assert self.g5 == ClassA(True, True)
            assert self.g6 is None
            assert self.h1 == [ClassA(False, False)]
            assert self.h2 == [ClassA(True, True)]
            assert self.h3 == [ClassA(False, False)]
            assert self.h4 is None
            assert self.h5 == [ClassA(True, True)]
            assert self.h6 is None
            assert self.i1 == {"c": ClassA(False, False)}
            assert self.i2 == {"a": ClassA(True, True)}
            assert self.i3 == {"d": ClassA(False, False)}
            assert self.i4 is None
            assert self.i5 == {"b": ClassA(True, True)}
            assert self.i6 is None


    @dictparser
    class TopLevelDefauls:
        a2: None = None
        b2: bool = True
        b5: Optional[bool] = True
        b6: Optional[bool] = None
        c2: int = 1
        c5: Optional[int] = 2
        c6: Optional[int] = None
        d2: str = "default"
        d5: Optional[str] = "default"
        d6: Optional[str] = None

        def assert_defaults(self):  # pylint: disable=too-many-statements
            assert self.a2 is None
            assert self.b2 is True
            assert self.b5 is True
            assert self.b6 is None
            assert self.c2 == 1
            assert self.c5 == 2
            assert self.c6 is None
            assert self.d2 == "default"
            assert self.d5 == "default"
            assert self.d6 is None


    def test_defaults_only_empty_dict_from_method():
        """Tests @dictparser class construction from empty dict"""
        v = TopLevelDefauls.from_dict({}) # type: ignore
        v.assert_defaults()

        v2 = TopLevelDefauls.from_dict(v.as_dict()) # type: ignore
        v2.assert_defaults()

        assert v2 == v


    def test_defaults_only_empty_dict_from_free_func():
        """Tests @dictparser class construction from empty dict"""
        v = from_dict(TopLevelDefauls, {})
        v.assert_defaults()

        v2 = from_dict(TopLevelDefauls, as_dict(v))
        v2.assert_defaults()

        assert v2 == v


    def test_with_defaults_from_method():
        v = TopLevel.from_dict(TopLevel.get_construct_data()) # type: ignore
        v.assert_defaults()

        v2 = TopLevel.from_dict(v.as_dict()) # type: ignore
        v2.assert_defaults()

        assert v2 == v


    def test_with_defaults_from_free_func():
        v = from_dict(TopLevel, TopLevel.get_construct_data())
        v.assert_defaults()

        v2 = from_dict(TopLevel, as_dict(v))
        v2.assert_defaults()

        assert v2 == v


    def test_defaults_not_mutable_from_method():
        v = TopLevel.from_dict(TopLevel.get_construct_data()) # type: ignore
        v.e1.append(6)
        v.e2.append(6)
        v.e3.append(6) # type: ignore
        v.e5.append(6) # type: ignore
        v.f1["c"] = 7
        v.f2["c"] = 7
        v.f3["c"] = 7 # type: ignore
        v.f5["c"] = 7 # type: ignore
        v.g1.extra = True
        v.g2.extra = False
        v.g3.extra = True # type: ignore
        v.g5.extra = False # type: ignore
        v.h1.append(ClassA(True, False))
        v.h1[0].extra = True
        v.h2.append(ClassA(True, False))
        v.h2[0].extra = False
        v.h3.append(ClassA(True, False)) # type: ignore
        v.h3[0].extra = True # type: ignore
        v.h5.append(ClassA(True, False)) # type: ignore
        v.h5[0].extra = False # type: ignore
        v.i1["x"] = ClassA(True, False)
        v.i1["c"].extra = True
        v.i2["x"] = ClassA(True, False)
        v.i2["a"].extra = False
        v.i3["x"] = ClassA(True, False) # type: ignore
        v.i3["d"].extra = True # type: ignore
        v.i5["x"] = ClassA(True, False) # type: ignore
        v.i5["b"].extra = False # type: ignore

        v2 = TopLevel.from_dict(TopLevel.get_construct_data()) # type: ignore
        v2.assert_defaults()


    def test_defaults_not_mutable_from_free_func():
        v = from_dict(TopLevel, TopLevel.get_construct_data())
        v.e1.append(6)
        v.e2.append(6)
        v.e3.append(6) # type: ignore
        v.e5.append(6) # type: ignore
        v.f1["c"] = 7
        v.f2["c"] = 7
        v.f3["c"] = 7 # type: ignore
        v.f5["c"] = 7 # type: ignore
        v.g1.extra = True
        v.g2.extra = False
        v.g3.extra = True # type: ignore
        v.g5.extra = False # type: ignore
        v.h1.append(ClassA(True, False))
        v.h1[0].extra = True
        v.h2.append(ClassA(True, False))
        v.h2[0].extra = False
        v.h3.append(ClassA(True, False)) # type: ignore
        v.h3[0].extra = True # type: ignore
        v.h5.append(ClassA(True, False)) # type: ignore
        v.h5[0].extra = False # type: ignore
        v.i1["x"] = ClassA(True, False)
        v.i1["c"].extra = True
        v.i2["x"] = ClassA(True, False)
        v.i2["a"].extra = False
        v.i3["x"] = ClassA(True, False) # type: ignore
        v.i3["d"].extra = True # type: ignore
        v.i5["x"] = ClassA(True, False) # type: ignore
        v.i5["b"].extra = False # type: ignore

        v2 = from_dict(TopLevel, TopLevel.get_construct_data())
        v2.assert_defaults()
