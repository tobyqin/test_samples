# -*- coding: utf-8 -*-
"""
To generate xml:
py.test --junitxml results.xml tests.py
"""
from faker import Faker
import logging
import sys

fake = Faker()
logging.basicConfig(stream=sys.stdout)

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        print('hello, test me')
        self.fail("shouldn't happen")

    def test_pass(self):
        print('hello, test 1')
        print('hello, test 中')
        print('hello, test 哈哈')
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        self.assertEqual(11, 7 + 3)
