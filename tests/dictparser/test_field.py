# pylint: disable=line-too-long
from typing import Optional, List, Dict

import dictparser


@dictparser.dictparser()
class ClassABase:
    enable: bool


@dictparser.dictparser()
class ClassA(ClassABase):
    extra: bool


@dictparser.dictparser(kw_only=True)
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
    g7: ClassA = {"enable": True, "extra": True}  # type: ignore [reportAssignmentType]
    g3: Optional[ClassA]
    g4: Optional[ClassA]
    g5: Optional[ClassA] = ClassA(True, True)
    g6: Optional[ClassA] = None
    g8: Optional[ClassA] = {"enable": True, "extra": True}  # type: ignore [reportAssignmentType]
    h1: List[ClassA]
    h2: List[ClassA] = [ClassA(True, True)]
    h7: List[ClassA] = [{"enable": True, "extra": True}]  # type: ignore [reportAssignmentType]
    h3: Optional[List[ClassA]]
    h4: Optional[List[ClassA]]
    h5: Optional[List[ClassA]] = [ClassA(True, True)]
    h6: Optional[List[ClassA]] = None
    h8: Optional[List[ClassA]] = [{"enable": True, "extra": True}]  # type: ignore [reportAssignmentType]
    i1: Dict[str, ClassA]
    i2: Dict[str, ClassA] = {"a": ClassA(True, True)}
    i7: Dict[str, ClassA] = {"a": {"enable": True, "extra": True}}  # type: ignore [reportAssignmentType]
    i3: Optional[Dict[str, ClassA]]
    i4: Optional[Dict[str, ClassA]]
    i5: Optional[Dict[str, ClassA]] = {"b": ClassA(True, True)}
    i6: Optional[Dict[str, ClassA]] = None
    i8: Optional[Dict[str, ClassA]] = {"b": {"enable": True, "extra": True}}  # type: ignore [reportAssignmentType]

    @classmethod
    def expected_fields(cls):
        return {
            "a1": {"field_type": None,                        "has_default": False},
            "a2": {"field_type": None,                        "has_default": True, "default_value": None},
            "b1": {"field_type": bool,                        "has_default": False},
            "b2": {"field_type": bool,                        "has_default": True, "default_value": True},
            "b3": {"field_type": Optional[bool],              "has_default": False},
            "b4": {"field_type": Optional[bool],              "has_default": False},
            "b5": {"field_type": Optional[bool],              "has_default": True, "default_value": True},
            "b6": {"field_type": Optional[bool],              "has_default": True, "default_value": None},
            "c1": {"field_type": int,                         "has_default": False},
            "c2": {"field_type": int,                         "has_default": True, "default_value": 1},
            "c3": {"field_type": Optional[int],               "has_default": False},
            "c4": {"field_type": Optional[int],               "has_default": False},
            "c5": {"field_type": Optional[int],               "has_default": True, "default_value": 2},
            "c6": {"field_type": Optional[int],               "has_default": True, "default_value": None},
            "d1": {"field_type": str,                         "has_default": False},
            "d2": {"field_type": str,                         "has_default": True, "default_value": "default"},
            "d3": {"field_type": Optional[str],               "has_default": False},
            "d4": {"field_type": Optional[str],               "has_default": False},
            "d5": {"field_type": Optional[str],               "has_default": True, "default_value": "default"},
            "d6": {"field_type": Optional[str],               "has_default": True, "default_value": None},
            "e1": {"field_type": List[int],                   "has_default": False},
            "e2": {"field_type": List[int],                   "has_default": True, "default_value": [1, 2, 3]},
            "e3": {"field_type": Optional[List[int]],         "has_default": False},
            "e4": {"field_type": Optional[List[int]],         "has_default": False},
            "e5": {"field_type": Optional[List[int]],         "has_default": True, "default_value": [1, 2, 3]},
            "e6": {"field_type": Optional[List[int]],         "has_default": True, "default_value": None},
            "f1": {"field_type": Dict[str, int],              "has_default": False},
            "f2": {"field_type": Dict[str, int],              "has_default": True, "default_value": {"a": 1}},
            "f3": {"field_type": Optional[Dict[str, int]],    "has_default": False},
            "f4": {"field_type": Optional[Dict[str, int]],    "has_default": False},
            "f5": {"field_type": Optional[Dict[str, int]],    "has_default": True, "default_value": {"b": 2}},
            "f6": {"field_type": Optional[Dict[str, int]],    "has_default": True, "default_value": None},
            "g1": {"field_type": ClassA,                      "has_default": False},
            "g2": {"field_type": ClassA,                      "has_default": True, "default_value": ClassA(True, True)},
            "g3": {"field_type": Optional[ClassA],            "has_default": False},
            "g4": {"field_type": Optional[ClassA],            "has_default": False},
            "g5": {"field_type": Optional[ClassA],            "has_default": True, "default_value": ClassA(True, True)},
            "g6": {"field_type": Optional[ClassA],            "has_default": True, "default_value": None},
            "g7": {"field_type": ClassA,                      "has_default": True, "default_value": ClassA(True, True)},
            "g8": {"field_type": Optional[ClassA],            "has_default": True, "default_value": ClassA(True, True)},
            "h1": {"field_type": List[ClassA],                "has_default": False},
            "h2": {"field_type": List[ClassA],                "has_default": True, "default_value": [ClassA(True, True)]},
            "h3": {"field_type": Optional[List[ClassA]],      "has_default": False},
            "h4": {"field_type": Optional[List[ClassA]],      "has_default": False},
            "h5": {"field_type": Optional[List[ClassA]],      "has_default": True, "default_value": [ClassA(True, True)]},
            "h6": {"field_type": Optional[List[ClassA]],      "has_default": True, "default_value": None},
            "h7": {"field_type": List[ClassA],                "has_default": True, "default_value": [ClassA(True, True)]},
            "h8": {"field_type": Optional[List[ClassA]],      "has_default": True, "default_value": [ClassA(True, True)]},
            "i1": {"field_type": Dict[str, ClassA],           "has_default": False},
            "i2": {"field_type": Dict[str, ClassA],           "has_default": True, "default_value": {"a": ClassA(True, True)}},
            "i3": {"field_type": Optional[Dict[str, ClassA]], "has_default": False},
            "i4": {"field_type": Optional[Dict[str, ClassA]], "has_default": False},
            "i5": {"field_type": Optional[Dict[str, ClassA]], "has_default": True, "default_value": {"b": ClassA(True, True)}},
            "i6": {"field_type": Optional[Dict[str, ClassA]], "has_default": True, "default_value": None},
            "i7": {"field_type": Dict[str, ClassA],           "has_default": True, "default_value": {"a": ClassA(True, True)}},
            "i8": {"field_type": Optional[Dict[str, ClassA]], "has_default": True, "default_value": {"b": ClassA(True, True)}},
        }


def test_available_fields():
    fields = dictparser.fields(TopLevel)

    assert set(field.field_name for field in fields) == TopLevel.expected_fields().keys()

    for field in fields:
        print(field, field.field_type)
        expected = TopLevel.expected_fields()[field.field_name]

        assert field.field_name == field.data_key
        assert field.field_type == expected["field_type"]
        assert field.has_default == expected["has_default"]
        assert field.is_required == (not expected["has_default"])

        if expected["has_default"]:
            assert field.get_default_value() == expected["default_value"]
