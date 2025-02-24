## Flask API

This API returns mean and median values given a list of integer values.

Example requests and results:

`curl http://localhost:8085/stat/mean \
-X POST -H “Content-Type: application/json” \ -d ‘{“data”:[1,1,2,3,5]}’`

`> {“data”: [1,1,2,3,5], “result”: 2.4}`

`curl http://localhost:8085/stat/median \ -H “Content-Type: text/csv” -X POST \ -d ‘1,1,2,3,5’`

`> {“data”: [1,1,2,3,5], “result”: 2}`

The service is executed by running a Flask app from a virtual environment using Docker.

### Setup

Create a Python 3.12.9 environment (e.g., `flask-mean-median`).


`pip install -r flask_mean_median/requirements.txt`

### Docker

build:

`docker build -t flask_mean_median .`

get images:

`docker images`

run:

`docker run -d -p 5000:5000 --name flask-mean-median flask_mean_median`

### Testing

pytest:

`pytest flask_mean_median/test_api.py`

Docker:

`docker ps` (for retreiving container ID)

`docker exec -it <container_id> py.test`