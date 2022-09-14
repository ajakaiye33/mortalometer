install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	#format code
	black *.py mortalcalculator/*.py
lint:   #lint code
	pylint --disable=R,C,W0621 *.py mortalcalculator/*.py
test:
	#test
	pytest mortalcalculator/test_mortality_calculate.py 
clean:
	#clean caches
	rm -rf __pycache__ .pytest_cache
build:
	#build container
	#docker build -t deploy-fastapi .
run:
	#run container
	#docker run -p 127.0.01:8080:8080 cla36
deploy:
	#deploy
all:install format lint test clean
