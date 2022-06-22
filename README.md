# Test_Python

Task register's app

1. How To launch :

  * python3 app/app.py

  * server :
    http://127.0.0.1
  * port :
    5000

  * API :
    - POST /task  {"name":"Task example","priority":"1","description":"task 1 test"}
    - GET /task
    - GET /task?sortby=(priority|creation_date|last_update)
    - GET /task/{id}
    - PUT /task/{id}
    - DELETE /task/{id}

  * example :
      - curl -X POST http://127.0.0.1:5000/task -H "Content-Type:application/json" -d '{"name":"Task example","priority":1,"description":"task 1 test"}'


2. Unit Test :
  python3 app/test_unit.py


3. Makefile :
  * make
    - all:
      install launch_api launch_test

    - install:
	    pip3 install -r requirements.txt

    - launch_api:
	    python3 app/app.py

    - launch_test:
	    python3 app/test_unit.py


4. Dockerfile :
  - docker build -t my_app .
  - docker run -d -p 5000:5000 my_app
