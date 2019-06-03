[![Build Status](https://travis-ci.org/bitpanda-labs/bind.svg?branch=master)](https://travis-ci.org/bitpanda-labs/bind)

# bind

<!--- Don't edit the version line below manually. Let bump2version do it for you. -->
> Version 2.1.0

> bind is a function that joins strings in a way we often need

## Usage

```python
from bind import bind
things_to_bind = ['castable', 'to', 's t r i n g.', 45, '"hi"', 0.25]

# defaults for urllib.parse.quote_plus, leaving these out would change nothing
kwargs = dict(safe='', encoding=None, errors=None) 

# by default, use slash separator and urlencoding
bind(*things_to_bind, **kwargs)
'castable/to/s+t+r+i+n+g./45/%22hi%22/0.25'

# turn off url encoding
bind(*things_to_bind, url=False, **kwargs)
'castable/to/s t r i n g./45/"hi"/0.25'

# result is the same if you pass in a list
bind(things_to_bind, url=False, **kwargs)
'castable/to/s t r i n g./45/"hi"/0.25'

# change separator --- note that it strips the other . in things_to_bind[2]
bind(*things_to_bind, sep='.')
'castable.to.s+t+r+i+n+g.45.%22hi%22.0.25'

# pointless but possible, and will strip W, H and Y from items in iterable!
bind(*things_to_bind, sep='WHY', url=True, **kwargs)
'castableWHYtoWHYs+t+r+i+n+g.WHY45WHY%22hi%22WHY0.25'
```

Aside from `url=bool` and `sep=str`, all keyword arguments are passed to [`urllib.parse.quote_plus`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote_plus)

## Tests (300% coverage)

```bash
coverage run -m unittest
coverage report --omit=tests/*
```

```
Name               Stmts   Miss  Cover
--------------------------------------
bind/__init__.py       2      0   100%
bind/bind.py          10      0   100%
--------------------------------------
TOTAL                 12      0   100%
```
