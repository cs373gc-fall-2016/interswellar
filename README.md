# interswellar
spaaace

# Local development

Set up your environment:
```
git clone git@github.com:TheFireFerret/interswellar.git
cd interswellar
pyvenv-3.5 ~/interswellar
source ~/interswellar/bin/activate
pip install -r requirements.txt
```

Run locally:
```
python application.py
```

# Deploy to AWS

First, install the elastic beanstalk shell (not in the interstellar venv)
```
deactivate
pip install --upgrade --user awsebcli
```

Add `~/.local/bin` to your path in your .bashrc or .zsh
```
export PATH=~/.local/bin:$PATH
```

Verify eb is installed:
```
eb --version
```

Initialize shell
```
eb init
```

This will start a bunch of questions: 
Region: Select US East
AWS key: <AWS Key>
Secret Key: <Secret Key>
Application: interswellar
Platform: Python
Version: Python 3.4 (first one)
SSH: yes
Keypair: aws-eb

Next hook up the git branch:
```
eb use interswellar-prod
```

After commiting code changes, run
```
eb deploy
```

Please do not deploy non-working code. Test locally first.
