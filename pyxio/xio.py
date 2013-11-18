# -*- coding: utf-8 -*-

import os

try:
    import bz2
except ImportError:
    bz2 = None

try:
    import gzip
except ImportError:
    gzip = None


def xopen(path, mode='r'):
    # specifal path
    if path == '-':
        if mode.startswith('r'):
            path = '/dev/stdin'
        else:
            path = '/dev/stdout'

        return open(path, mode)

    # *.bz2, *.gz
    ext = os.path.splitext(path)[1]

    if ext:
        ext = ext.lower()
        if ext == '.bz2':
            if bz2:
                return bz2.BZ2File(path, mode)
            else:
                raise Exception('bz2 module is not available.')

        elif ext == '.gz':
            if gzip:
                return gzip.open(path, mode)
            else:
                raise Exception('gzip module is not available.')

    #
    return open(path, mode)
