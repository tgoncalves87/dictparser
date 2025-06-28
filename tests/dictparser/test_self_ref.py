import sys

from typing import Optional, List
from dictparser import dictparser, from_dict, to_dict


@dictparser(kw_only=True)
class ClassA:
    name: str
    special_one: Optional['ClassA'] = None
    children: List['ClassA'] = []


if sys.version_info >= (3, 11):
    @dictparser(kw_only=True)
    class ClassA310:
        name: str
        special_one: 'ClassA310 | None' = None
        children: list['ClassA310'] = []


def test_unions():
    if sys.version_info >= (3, 11):
        classes = [ClassA, ClassA310]
    else:
        classes = [ClassA]

    for cls in classes:
        initial_data = {
            'name': '1',
            'special_one': {'name': 'special-1'},
            'children': [
                {'name': '1.1'},
                {'name': '1.2'}
            ]
        }

        assert to_dict(from_dict(cls, initial_data)) == {
            'name': '1',
            'special_one': {'name': 'special-1', 'special_one': None, 'children': []},
            'children': [
                {'name': '1.1', 'special_one': None, 'children': []},
                {'name': '1.2', 'special_one': None, 'children': []},
            ]
        }
