""" The views for the app """
# pylint: disable=unused-import
from interswellar import app
from flask import Flask, render_template
import requests, json
from collections import defaultdict


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
    	sami_commits=commits['TheFireFerret'],
    	denise_commits=commits.get('denisely',0),
    	young_commits=commits['jedyobidan'],
    	david_commits=commits['dshimo'],
    	nathan_commits=commits['nazopo'],
    	charlotte_issues=issues.get('charharharhar', 0),
    	sami_issues=issues['TheFireFerret'],
    	denise_issues=issues.get('denisely',0),
    	young_issues=issues['jedyobidan'],
    	david_issues=issues.get('dshimo',0),
    	nathan_issues=issues['nazopo'])

def get_commits():
	url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/stats/contributors'
	response = requests.get(url).text
	parsed = json.loads(response)
	return {user['author']['login'] : user['total'] for user in parsed}

def get_issues():
	url = 'https://api.github.com/repos/cs373gc-fall-2016/interswellar/issues?state=all'
	response = requests.get(url).text
	parsed = json.loads(response)
	num_issues = defaultdict(int)
	for issue in parsed:
		if 'pull_request' not in issue:
			num_issues[issue['user']['login']] += 1
	return num_issues


