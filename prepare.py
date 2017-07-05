# -*- coding: utf-8 -*-

import logging
import sys
from codecs import open
from time import sleep

from faker import Faker

fake = Faker()
logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO)

content = ''
test_file = 'tests.py'
counter = {'passed': 0, 'failed': 0, 'skipped': 0}
error_types = ['SystemError', 'AssertionError', 'ValueError', 'KeyError', 'EnvironmentError']


def log_some_message():
    for i in range(fake.random_int(10)):
        if fake.boolean(80):
            logging.info(fake.text())
        if fake.boolean(10):
            logging.warning(fake.text())
        if fake.boolean(5):
            logging.error(fake.text())


def wait_some_time():
    seconds = fake.random_int(200) / 100
    sleep(seconds)


def get_test_template():
    return u"""# -*- coding: utf-8 -*-
'''
To generate xml:
py.test --junitxml results.xml tests.py
'''
from prepare import *

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):

"""


def add_pass_test():
    tpl = u"""    def test_pass_{}(self):
        log_some_message()
        wait_some_time()
        self.assertEqual(10, 7 + 3)

"""
    counter['passed'] += 1
    return tpl.format(counter['passed'])


def add_skip_test():
    tpl = u"""    @unittest.skip("{}")
    def test_skipped_{}(self):
        self.fail("shouldn't happen")

"""
    counter['skipped'] += 1
    return tpl.format(fake.sentence(), counter['skipped'])


def add_fail_test():
    tpl = u"""    def test_fail_{}(self):
        log_some_message()
        wait_some_time()
        raise {}('{}')

"""
    counter['failed'] += 1
    error = fake.random.choice(error_types)
    return tpl.format(counter['failed'], error, fake.sentence())


def prepare():
    content = get_test_template()

    for i in range(100):
        if fake.boolean(80):
            content += add_pass_test()
        if fake.boolean(10):
            content += add_fail_test()
        if fake.boolean(5):
            content += add_skip_test()

    with open(test_file, mode='w', encoding='utf8') as f:
        f.write(content)


if __name__ == '__main__':
    prepare()
