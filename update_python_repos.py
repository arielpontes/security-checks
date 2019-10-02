import json
import requests
import subprocess

from settings import TOKEN

PER_PAGE = 100

page = 1

headers = {'Authorization': f'token {TOKEN}'}

repos = requests.get(
    'https://api.github.com/orgs/eea/repos',
    params={'page': page, 'per_page': PER_PAGE},
    headers=headers
)
repo_list = []
while True:
    for repo in repos.json():
        if repo['language'] == 'Python':
            repo_list.append(repo['name'])
            print(repo['name'])
    if 'next' not in repos.links:
        break
    page += 1
    repos = requests.get(
        repos.links['next']['url'],
        params={'page': page, 'per_page': PER_PAGE},
        headers=headers
    )
with open('python_repos.txt', 'w+') as f:
    f.write('\n'.join(repo_list))
