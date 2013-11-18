#!/bin/env/python2.7
# -*- coding: utf-8 -*-

import contextlib
import os
import tempfile
import unittest
import pyxio.xio


class XioTest(unittest.TestCase):
    def test_xopen_bzip2_read(self):
        with pyxio.xio.xopen(self._get_path('bzip2.bz2')) as fin:
            self.assertEquals(fin.read(), 'Hello World')

    def test_xopen_bzip2_write(self):
        with tempfile.NamedTemporaryFile(suffix='.bz2') as tf:
            with pyxio.xio.xopen(tf.name, 'w') as fout:
                fout.write('Hello World')

            with pyxio.xio.xopen(tf.name) as fin:
                self.assertEquals(fin.read(), 'Hello World')

    def test_xopen_bzip2_read_disabled(self):
        with self._disable_module('bz2'):
           self.assertRaises(Exception, pyxio.xio.xopen, self._get_path('bzip2.bz2'))

    def test_xopen_bzip2_write_disabled(self):
        with tempfile.NamedTemporaryFile(suffix='.bz2') as tf:
            with self._disable_module('bz2'):
               self.assertRaises(Exception, lambda f: pyxio.xio.xopen(f, 'w'), tf.name)

    def test_xopen_gzip_read(self):
        with pyxio.xio.xopen(self._get_path('gzip.gz')) as fin:
            self.assertEquals(fin.read(), 'Hello World')

    def test_xopen_gzip_write(self):
        with tempfile.NamedTemporaryFile(suffix='.gz') as tf:
            with pyxio.xio.xopen(tf.name, 'w') as fout:
                fout.write('Hello World')

            with pyxio.xio.xopen(tf.name) as fin:
                self.assertEquals(fin.read(), 'Hello World')

    def test_xopen_gzip_read_disabled(self):
        with self._disable_module('gzip'):
            self.assertRaises(Exception, pyxio.xio.xopen, self._get_path('gzip.gz'))

    def test_xopen_gzip_write_disabled(self):
        with self._disable_module('gzip'):
           self.assertRaises(Exception, lambda f: pyxio.xio.xopen(f, 'w'), self._get_path('gzip.gz'))

    def test_xopen_uncompressed_read(self):
        with pyxio.xio.xopen(self._get_path('uncompressed.txt')) as fin:
            self.assertEquals(fin.read(), 'Hello World')

    def test_xopen_uncompressed_write(self):
        with tempfile.NamedTemporaryFile() as tf:
            with pyxio.xio.xopen(tf.name, 'w') as fout:
                fout.write('Hello World')

            with pyxio.xio.xopen(tf.name) as fin:
                self.assertEquals(fin.read(), 'Hello World')

    def test_xopen_stdin_read(self):
        with pyxio.xio.xopen('/dev/stdin') as fin:
            self.assertEquals(fin.name, '/dev/stdin')

        with pyxio.xio.xopen('-') as fin:
            self.assertEquals(fin.name, '/dev/stdin')

    def test_xopen_stdout_write(self):
        with pyxio.xio.xopen('/dev/stdout', 'w') as fin:
            self.assertEquals(fin.name, '/dev/stdout')

        with pyxio.xio.xopen('-', 'w') as fin:
            self.assertEquals(fin.name, '/dev/stdout')

    def test_xopen_stderr_write(self):
        with pyxio.xio.xopen('/dev/stderr', 'w') as fin:
            self.assertEquals(fin.name, '/dev/stderr')

    def _get_path(self, name):
        return os.path.join(os.path.dirname(__file__), name)

    @contextlib.contextmanager
    def _disable_module(self, name):
        mod = getattr(pyxio.xio, name)
        setattr(pyxio.xio, name, None)
        yield

        setattr(pyxio.xio, name, mod)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))

    return suite


if __name__ == '__main__':
    unittest.main()
