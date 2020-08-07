"""
Bind: a Python module to mimic os.path.join without reverting to root
"""

from urllib.parse import quote_plus
from typing import Union, Optional


def bind(*args: Union[str, list, set, tuple],
         sep: str = '/',
         url: bool = True,
         safe: str = ':/',
         encoding: Optional[str] = None,
         errors: Optional[str] = None) -> str:
    if isinstance(args[0], (list, set, tuple)):
        parts = [i for i in args[0] if i is not False and i is not None]
    else:
        parts = [i for i in args if i is not False and i is not None]

    if url:
        processed_parts = (quote_plus(str(arg).strip(sep), safe=safe, encoding=encoding, errors=errors)
                           for arg in parts)
    else:
        processed_parts = (str(arg).strip(sep) for arg in parts)

    return sep.join(processed_parts)
