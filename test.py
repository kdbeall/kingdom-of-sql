#!/usr/bin/python3

import unittest

class TestExample(unittest.TestCase):
    def test_equal(self):
        self.assertEqual("Foo", "Foo")