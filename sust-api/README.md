## Flask web service

This API returns mean and median values given a list of integer values.

Example requests and results:

`curl http://localhost:8085/stat/mean \
-X POST -H “Content-Type: application/json” \ -d ‘{“data”:[1,1,2,3,5]}’`

`> {“data”: [1,1,2,3,5], “result”: 2.4}`

`curl http://localhost:8085/stat/median \ -H “Content-Type: text/csv” -X POST \ -d ‘1,1,2,3,5’`

`> {“data”: [1,1,2,3,5], “result”: 2}`

The service is executed by running a Flask app from a virtual environment using Docker.

Postman was used to test.

### Docker

build:

`docker build -t sust-api .`

get images:

`docker images`

run:

`docker run -d -p 5000:5000 --name python-restapi sust-api`

### Testing

pytest:

`pytest test_sust_app.py`

Docker:

`docker ps` (for retreiving container ID)

`docker exec -it <container_id> py.test`