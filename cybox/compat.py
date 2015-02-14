import sys

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)


if is_py2:
    from StringIO import StringIO
    basestring = basestring
    bytes = str
    long = long
    str = unicode

elif is_py3:
    from io import StringIO
    basestring = (str, bytes)
    bytes = bytes
    long = int
    str = str


class UnicodeMixin(object):
    """Make String functions work on Python 2 and 3.

    Classes using this mixin must define a `__unicode__` function that returns
    the Unicode representation of the object (as a `str` on Python 3 and a
    `unicode` on Python 2).

    Python 2 will use `__unicode__()` directly for `unicode()` calls, and
    encode the output in UTF-8 when the `str()` function is called.

    Python 3 will use `__unicode__()` indirectly when `str()` is called.

    This code was adapted from:
        http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/
    """
    if is_py3:
        __str__ = lambda x: x.__unicode__()
    else:
        __str__ = lambda x: x.__unicode__().encode('utf-8')