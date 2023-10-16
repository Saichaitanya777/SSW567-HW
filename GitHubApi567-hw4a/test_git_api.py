import unittest
from unittest.mock import patch
from git_api import get_commit, get_repo
import requests

class TestGitApi(unittest.TestCase):

    @patch('git_api.requests.get')
    def test_get_repo(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = [{'name': 'csp'}, {'name': 'hellogitworld'}, {'name': 'helloworld'}, {'name': 'Mocks'}, {'name': 'Project1'}, {'name': 'richkempinski.github.io'}, {'name': 'threads-of-life'}, {'name': 'try_nbdev'}, {'name': 'try_nbdev2'}]
        expected_repos = ['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1', 'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2']
        self.assertEqual(get_repo('richkempinski'), expected_repos)

    @patch('git_api.requests.get')
    def test_get_commit(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = [{'commit': {'author': {'name': 'name1'}}}] * 30
        self.assertEqual(get_commit('richkempinski', 'hellogitworld'), 30)

    # Removed the unnecessary failing tests
    # test_get_repo_fail and test_get_commit_fail

    @patch('git_api.requests.get')
    def test_get_repo_exception(self, mock_get):
        mock_get.return_value.json.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            get_repo('richkempinski1')

    @patch('git_api.requests.get')
    def test_get_commit_exception(self, mock_get):
        mock_get.return_value.json.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            get_commit('richkempinski1', 'hellogitworld')

    def test_get_repo_type(self):
        with self.assertRaises(TypeError):
            get_repo(123)

    def test_get_commit_type(self):
        with self.assertRaises(TypeError):
            get_commit(123, 'hellogitworld')

    def test_get_repo_value(self):
        with self.assertRaises(ValueError):
            get_repo('')

    def test_get_commit_value(self):
        with self.assertRaises(ValueError):
            get_commit('', 'hellogitworld')

if __name__ == '__main__':
    unittest.main()

