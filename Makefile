install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	#format code
	black *.py mortalcalculator/*.py
lint:   #lint code
	pylint --disable=R,C *.py mortalcalculator/*.py
test:
	#test
	pytest mortalcalculator/test_mortality_calculate.py 
build:
	#build container
	#docker build -t deploy-fastapi .
run:
	#run container
	#docker run -p 127.0.01:8080:8080 cla36
deploy:
	#deploy
all:
	#run all
	install format lint test 
