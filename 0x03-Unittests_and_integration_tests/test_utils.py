#!/usr/bin/env python3
"""Tests for utilss"""
import unittest
from parameterized import parameterized, parameterized_class
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Class to test Access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test access nested map exceptions"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
