# interswellar [![Build Status](https://travis-ci.org/TheFireFerret/interswellar.svg?branch=master)](https://travis-ci.org/TheFireFerret/interswellar)
spaaace  

http://interswellar.me
http://interswellar-prod.us-east-1.elasticbeanstalk.com

# Local development

Set up your environment:
```
sudo apt-get install -y python-virtualenv
virtualenv -p python3.4 ~/venv/interswellar
```

Get the code and install dependencies:
```
git clone git@github.com:TheFireFerret/interswellar.git
cd interswellar
source ~/venv/interswellar/bin/activate
pip install -r requirements.txt
deactivate
```

To run locally, first make sure you are in your virtualenv (if not, run 
`source ~/venv/interswellar/bin/activate`). Then:
```
python application.py
```
(Control-C to quit the app)


# Manually deploy changes to AWS (not recommended)

This is not the recommended way to deploy code. The recommended way to deploy
code is through Travis CI; so only use this method if Travis is broken or we
haven't set it up yet.

If you are still in the interswellar virtualenv, get out of it by running 
`deactivate`

Set up your environment:
```
pip install --upgrade --user awsebcli
export PATH=~/.local/bin:$PATH
```
Note that you should add the export line to your .bashrc or .zsh to have your 
path set correctly each time.

Initialize eb (can run multiple times if you screw up)
```
eb init -i
```

You will now take a quiz. Here are the answers:

* Region: US East
* AWS key: `<AWS Key>`
* Secret Key: `<Secret Key>`
* Application: interswellar
* Platform: Python
* Version: Python 3.4 (first one)
* SSH: yes
* Keypair: aws-eb

Our API key and secret key can be found in the Slack.


To deploy the code, first make sure it is passing all tests and looks okay 
locally. Additionally, we will only deploy from the master branch, so merge
your code accordingly.

```
git checkout master
git pull --ff-only origin master
export interswellar_latest=$(eb status | grep "Deployed Version:" | sed 's/\s*Deployed Version:\s*//')
eb deploy interswellar-prod
eb open interswellar-prod
```

Verify your changes on the site. If everything looks good, you're done! If 
something looks broken, roll back the changes:

```
eb deploy --version $interswellar_latest interswellar-prod
```

Please do not deploy non-working code. Test locally first.
