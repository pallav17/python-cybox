import sys

import six

if six.PY2:
    from StringIO import StringIO
    basestring = basestring
    bytes = str
    long = long
    str = unicode
    chars = lambda x: x
    def xor(data, key):
        key = int(key)
        return b''.join([chr(ord(c) ^ key) for c in chars(data)])

elif six.PY3:
    from io import StringIO
    basestring = (str, bytes)
    bytes = bytes
    long = int
    str = str
    chars = lambda x: [chr(y) for y in x]
    def xor(data, key):
        key = int(key)
        b = bytearray(data)
        for i in range(len(b)):
            b[i] ^= key
        return bytes(b)
