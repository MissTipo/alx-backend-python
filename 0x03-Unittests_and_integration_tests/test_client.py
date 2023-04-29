#!/usr/bin/env python3
"""
Contains a class and functions that parameterize and patch as decorators,
Mock a property, Integration test: fixtures, Integration tests
"""

import unittest
from unittest.mock import patch, PropertyMock
from urllib.error import HTTPError
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Contains the test methods for GithubOrgClient.org"""
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """ test that GithubOrgClient.org returns the correct value """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """ to unit-test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "NissTipo"}) as mock_get:
            test_json = {"repos_url": "MissTipo"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            # mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "MissTipo"}])
    def test_public_repos(self, mock_get):
        """ performs unit-test on GithubOrgClient.public_repos method """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("MissTipo")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["MissTipo"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_return):
        """ to unit-test GithubOrgClient.has_license """
        test_client = GithubOrgClient("MissTipo")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Mock code that sends external request """
    @classmethod
    def setUpClass(cls):
        """ It is part of the unittest.TestCase API
        method to return example payloads found in the fixtures """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ It is part of the unittest.TestCase API
        method to stop the patcher """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ method to test GithubOrgClient.public_repos """
        test_class = GithubOrgClient("MissTipo")
        assert True

    def test_public_repos_with_license(self):
        """ method to test the public_repos with the argument license """
        test_class = GithubOrgClient("MissTipo")
        assert True
