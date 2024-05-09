from dictparser import dictparser


@dictparser
class ClassABase:
    enable: bool


@dictparser
class ClassA(ClassABase):
    extra: bool


@dictparser
class TopLevel:
    a1: None
    a2: None = None
    b1: bool
    b2: bool = True
    b3: bool | None
    b4: bool | None
    b5: bool | None = True
    b6: bool | None = None
    c1: int
    c2: int = 1
    c3: int | None
    c4: int | None
    c5: int | None = 2
    c6: int | None = None
    d1: str
    d2: str = "default"
    d3: str | None
    d4: str | None
    d5: str | None = "default"
    d6: str | None = None
    e1: list[int]
    e2: list[int] = [1, 2, 3]
    e3: list[int] | None
    e4: list[int] | None
    e5: list[int] | None = [1, 2, 3]
    e6: list[int] | None = None
    f1: dict[str, int]
    f2: dict[str, int] = {"a": 1}
    f3: dict[str, int] | None
    f4: dict[str, int] | None
    f5: dict[str, int] | None = {"b": 2}
    f6: dict[str, int] | None = None
    g1: ClassA
    g2: ClassA = ClassA(True, True)
    g3: ClassA | None
    g4: ClassA | None
    g5: ClassA | None = ClassA(True, True)
    g6: ClassA | None = None
    h1: list[ClassA]
    h2: list[ClassA] = [ClassA(True, True)]
    h3: list[ClassA] | None
    h4: list[ClassA] | None
    h5: list[ClassA] | None = [ClassA(True, True)]
    h6: list[ClassA] | None = None
    i1: dict[str, ClassA]
    i2: dict[str, ClassA] = {"a": ClassA(True, True)}
    i3: dict[str, ClassA] | None
    i4: dict[str, ClassA] | None
    i5: dict[str, ClassA] | None = {"b": ClassA(True, True)}
    i6: dict[str, ClassA] | None = None


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
    b5: bool | None = True
    b6: bool | None = None
    c2: int = 1
    c5: int | None = 2
    c6: int | None = None
    d2: str = "default"
    d5: str | None = "default"
    d6: str | None = None

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


def test_defaults_only_empty_dict():
    """Tests @dictparser class construction from empty dict"""
    v = TopLevelDefauls.from_dict({})
    v.assert_defaults()

    v2 = TopLevelDefauls.from_dict(v.as_dict())
    v2.assert_defaults()

    assert v2 == v


def test_with_defaults():
    v = TopLevel.from_dict(TopLevel.get_construct_data())
    v.assert_defaults()

    v2 = TopLevel.from_dict(v.as_dict())
    v2.assert_defaults()

    assert v2 == v


def test_defaults_not_mutable():
    v = TopLevel.from_dict(TopLevel.get_construct_data())
    v.e1.append(6)
    v.e2.append(6)
    v.e3.append(6)
    v.e5.append(6)
    v.f1["c"] = 7
    v.f2["c"] = 7
    v.f3["c"] = 7
    v.f5["c"] = 7
    v.g1.extra = True
    v.g2.extra = False
    v.g3.extra = True
    v.g5.extra = False
    v.h1.append(True)
    v.h1[0].extra = True
    v.h2.append(True)
    v.h2[0].extra = False
    v.h3.append(True)
    v.h3[0].extra = True
    v.h5.append(True)
    v.h5[0].extra = False
    v.i1["x"] = True
    v.i1["c"].extra = True
    v.i2["x"] = True
    v.i2["a"].extra = False
    v.i3["x"] = True
    v.i3["d"].extra = True
    v.i5["x"] = True
    v.i5["b"].extra = False

    v2 = TopLevel.from_dict(TopLevel.get_construct_data())
    v2.assert_defaults()
