install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=sorc.main

format:	
	find . -type f -name "*.py" -exec black {} \;
	find . -type f -name "*.ipynb" -exec nbqa black {} \;

lint:
	find . -type f -name "*.py" -exec ruff check {} \;
	find . -type f -name "*.ipynb" -exec nbqa ruff {} \;


refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy








