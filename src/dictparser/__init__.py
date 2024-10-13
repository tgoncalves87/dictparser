__all__ = ['dictparser', 'from_dict', 'from_file', 'as_dict', 'fields', 'Field']

import sys

if sys.version_info >= (3, 11):
    from ._init_p311 import dictparser
    from ._init_p311 import from_dict
    from ._init_p311 import from_file
    from ._init_p311 import as_dict
    from ._init_p311 import fields
    from ._init_p311 import Field
else:
    from ._init_p36 import dictparser
    from ._init_p36 import from_dict
    from ._init_p36 import from_file
    from ._init_p36 import as_dict
    from ._init_p36 import fields
    from ._init_p36 import Field
