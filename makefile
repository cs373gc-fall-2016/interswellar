format:
	find . -type f \( -name "*.py" \) | xargs autopep8 -i

lint:
	find . -type f \( -name "*.py" -and -not -name "*_test.py" \) | xargs pylint -r n -d locally-disabled -d cyclic-import

test:
	coverage run --branch --source . -m unittest discover interswellar/ -p '*_test.py'
	coverage report -m

run:
	python application.py
