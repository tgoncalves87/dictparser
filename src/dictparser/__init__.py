import sys

__all__ = ['dictparser', 'from_dict', 'from_file', 'as_dict', 'fields']

if sys.version_info >= (3, 11):
    from ._init_p311 import dictparser
    from ._init_p311 import from_dict
    from ._init_p311 import from_file
    from ._init_p311 import as_dict
    from ._init_p311 import fields
else:
    from ._init_p36 import dictparser
    from ._init_p36 import from_dict
    from ._init_p36 import from_file
    from ._init_p36 import as_dict
    from ._init_p36 import fields
