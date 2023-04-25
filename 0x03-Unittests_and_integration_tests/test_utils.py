#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest import mock
import requests
from utils import access_nested_map, get_json
from typing import Mapping, Sequence, Union, Dict, List, Any, Tuple
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Derived class that contains the method to  test access_nested_map function
    """
    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a',], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        Calls the access_tested_map with the given input and asserts that the
        result is equal to the expected output
        """
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ['a']),
        ({'a': 1}, ['a', 'b'])
        ])
    def test_access_nested_map_exception(self, nested_map, expected_output):
        """"""
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """Contains the method to test utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    def test_get_json(self, test_url, test_payload):
        """Tests that utils.get_json returns the expected result"""
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """"""
    def test_memoize(self):
        """"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_a_method.assert_called_once()
