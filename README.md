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