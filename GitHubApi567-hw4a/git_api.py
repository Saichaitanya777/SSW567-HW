import requests


def get_repo(user_id):
    """Get the repo of the user"""
    if not isinstance(user_id, str):
        raise TypeError("Expected a string argument")
    if user_id == '':
        raise ValueError("Expected a non-empty string argument")

    url = 'https://api.github.com/users/{}/repos'.format(user_id)
    r = requests.get(url)
    repo_list = []
    for repo in r.json():
        repo_list.append(repo['name'])
    return repo_list


def get_commit(user_id, repo):
    """Get the commit of the user"""
    if not isinstance(user_id, str) or not isinstance(repo, str):
        raise TypeError("Expected string arguments for user and repo")
    if user_id == '' or repo == '':
        raise ValueError("Expected non-empty string arguments for user and repo")
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user_id, repo)
    r = requests.get(url)
    commit_list = []
    for commit in r.json():
        commit_list.append(commit['commit']['author']['name'])
    return len(commit_list)