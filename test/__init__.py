# -*- coding: utf-8 -*-

import unittest
import xio_test


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(xio_test.XioTest))

    return suite
