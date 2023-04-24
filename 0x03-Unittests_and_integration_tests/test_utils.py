#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from utils import access_nested_map
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
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected_output: Union[int, str, Dict, List]) -> Any:
        """
        Calls the access_tested_map with the given input and asserts that the
        result is equal to the expected output
        """
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected_output)
