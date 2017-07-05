# -*- coding: utf-8 -*-
"""
To generate xml:
py.test --junitxml results.xml tests.py
"""
import logging
import sys
from time import sleep

from faker import Faker

try:
    import unittest2 as unittest
except ImportError:
    import unittest

fake = Faker()
logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO)


def log_some_message():
    for i in range(0, fake.random_int(20)):
        if fake.boolean(80):
            logging.info(fake.text())
        if fake.boolean(10):
            logging.warning(fake.text())
        if fake.boolean(5):
            logging.error(fake.text())


def wait_some_time():
    seconds = fake.random_int(2000) / 100
    sleep(seconds)


class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        print('hello, test me')
        self.fail("shouldn't happen")

    def test_pass(self):
        log_some_message()
        wait_some_time()
        print('hello, test 哈哈')
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        log_some_message()
        wait_some_time()
        self.assertEqual(11, 7 + 3)
