"""
Bind: a one-line Python module to mimic os.path.join without reverting to root
"""

from urllib.parse import quote_plus


def bind(*args, sep='/', url=True, safe=':/', **kwargs): return sep.join(quote_plus(str(arg).strip(sep), safe=safe, **kwargs) if url else str(arg).strip(sep) for arg in (args[0] if isinstance(args[0], (list, set, tuple)) else (i for i in args if i)))
