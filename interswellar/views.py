""" The views for the app """
# pylint: disable=unused-import, bad-continuation, import-error
from collections import defaultdict
import json
import requests
from interswellar import app
from flask import Flask, render_template


@app.route('/')
def index():
    """ Returns splash page """
    return render_template('index.html')


@app.route('/about')
def about():
    """ Returns about page with commit and issues count"""
    commits = get_commits()
    issues = get_issues()
    return render_template('about.html',
        charlotte_commits=commits.get('charharharhar', 0),
        sami_commits=commits.get('TheFireFerret', 0),
        denise_commits=commits.get('denisely', 0),
        young_commits=commits.get('jedyobidan', 0),
        david_commits=commits.get('dshimo', 0),
        nathan_commits=commits.get('nazopo', 0),
        charlotte_issues=issues.get('charharharhar', 0),
        sami_issues=issues.get('TheFireFerret', 0),
        denise_issues=issues.get('denisely', 0),
        young_issues=issues.get('jedyobidan', 0),
        david_issues=issues.get('dshimo', 0),
        nathan_issues=issues.get('nazopo', 0))


def get_commits():
    """ gets number of commits for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/stats/contributors?client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    return {user['author']['login'] : user['total'] for user in parsed}


def get_issues():
    """ get number of issues for each team member """
    url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/issues?state=all&client_id=a857dda6c0869d2bc306&client_secret=e6f54c0cca99ebb7d6bfd5542052ed49638362ea'
    response = requests.get(url).text
    parsed = json.loads(response)
    num_issues = defaultdict(int)
    for issue in parsed:
        if 'pull_request' not in issue:
            num_issues[issue['user']['login']] += 1
    return num_issues