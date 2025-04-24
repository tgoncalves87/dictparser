from datetime import datetime

from typing import Optional
from dictparser import dictparser, from_dict, to_dict


@dictparser(kw_only=True)
class TopLevel:
    a1: datetime
    a2: datetime = datetime(2000, 1, 2)
    a3: Optional[datetime]
    a4: Optional[datetime]
    a5: Optional[datetime] = datetime(2000, 1, 5)
    a6: Optional[datetime] = None

    @classmethod
    def get_construct_data(cls):
        return {
            "a1": '2000-01-01T00:00:00',
            "a3": '2000-01-03T00:00:00',
            "a4": None,
        }

    def assert_construct_data(self):  # pylint: disable=too-many-statements
        assert self.a1 == datetime(2000, 1, 1)

    @classmethod
    def expected_dict(cls):  # pylint: disable=too-many-statements
        return {
            "a1": "2000-01-01T00:00:00",
            "a2": "2000-01-02T00:00:00",
            "a3": "2000-01-03T00:00:00",
            "a4": None,
            "a5": "2000-01-05T00:00:00",
            "a6": None,
        }


def test_datetime():
    v = from_dict(TopLevel, TopLevel.get_construct_data())
    v.assert_construct_data()

    assert to_dict(v) == TopLevel.expected_dict()
