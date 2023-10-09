import unittest

from git_api import get_commit, get_repo


class TestGitApi(unittest.TestCase):

    def test_get_repo(self):
        expected_repos = ['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1', 'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2']
        self.assertEqual(get_repo('richkempinski'), expected_repos)

    def test_get_commit(self):
        self.assertEqual(get_commit('richkempinski', 'hellogitworld'), 30)
        self.assertEqual(get_commit('richkempinski', 'helloworld'), 6)
        self.assertEqual(get_commit('richkempinski', 'Mocks'), 10)
        self.assertEqual(get_commit('richkempinski', 'Project1'), 2)
        self.assertEqual(get_commit('richkempinski', 'threads-of-life'), 1)
    
    def test_get_repo_fail(self):
        self.assertNotEqual(get_repo('richkempinski'), ['hellogitworld', 'helloworld', 'Mocks', 'Project1', 'threads-of-life', 'Test'])
    
    def test_get_commit_fail(self):
        self.assertNotEqual(get_commit('richkempinski', 'hellogitworld'), 31)
        self.assertNotEqual(get_commit('richkempinski', 'helloworld'), 7)
        self.assertNotEqual(get_commit('richkempinski', 'Mocks'), 11)
        self.assertNotEqual(get_commit('richkempinski', 'Project1'), 3)
        self.assertNotEqual(get_commit('richkempinski', 'threads-of-life'), 2)

    def test_get_repo_exception(self):
        with self.assertRaises(Exception):
            get_repo('richkempinski1')
    
    def test_get_commit_exception(self):
        with self.assertRaises(Exception):
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
