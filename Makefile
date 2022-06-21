all: install launch_api launch_test


install:
	pip3 install -r requirements.txt

launch_api:
	python3 api.py 

launch_test:
	python3 test_unit.py
