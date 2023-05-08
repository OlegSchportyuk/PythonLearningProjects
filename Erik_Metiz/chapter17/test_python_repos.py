import unittest

import python_repos_visual as prs

class PythonReposTestCase(unittest.TestCase):
    '''Тестирует python_repos_visual.py '''

    def test_get_response(self):
        self.r = prs.get_response()
        self.assertEqual(self.r.status_code, 200)

    def test_get_repo_dicts(self):
        self.repo_dicts = prs.get_repo_dicts(prs.get_response())
        self.assertEqual(len(self.repo_dicts), 30)

        self.repo_dict = self.repo_dicts[0]
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()
