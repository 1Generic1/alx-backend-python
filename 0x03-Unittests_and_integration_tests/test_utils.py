#!/usr/bin/env python3
""" test module """

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """ test module """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ test module """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ test module """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests `get_json`'s output."""
        with patch('utils.requests.get') as mocked_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mocked_get.return_value = mock_response
            result = get_json(test_url)
            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ test module """
    def test_memoize(self):
        """ test module """
        class TestClass:
            """ test module """
            def a_method(self):
                """ test module """
                return 42

                @memoize
                def a_property(self):
                    """ test module """
                    return self.a_method()
        with patch.object(TestClass, 'a_method') as mocked_method:
            instance = TestClass()
            result1 = instance.a_property()
            result2 = instance.a_property()
            mocked_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
