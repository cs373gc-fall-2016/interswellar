format:
	find . -type f \( -name "*.py" \) | xargs autopep8 -i

lint:
	find . -type f \( -name "*.py" -and -not -name "*_test.py" \) | xargs pylint -r n
test:
	coverage run --branch --source . -m unittest discover interswellar/ -p '*_test.py'
	coverage report -m

run:
	python application.py

pydoc:
	python -m pydoc -w interswellar
	python -m pydoc -w interswellar.views
	python -m pydoc -w interswellar.api
	python -m pydoc -w interswellar.api_test
	python -m pydoc -w interswellar.models_test
	python -m pydoc -w interswellar.views_test
	python -m pydoc -w interswellar.config
	