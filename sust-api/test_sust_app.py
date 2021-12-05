## unit test for sust-api
import pytest
from sust_app import app
from flask import json

## test cases
test_data = json.dumps([1,1,2,3,5])

## test and verify mean value
def test_mean():        
    response = app.test_client().post(
        '/stat/mean',
        data=test_data,
        content_type='application/json',
    )

    request_data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert request_data == 2.4

## test and verify mean value
def test_median():        
    response = app.test_client().post(
        '/stat/median',
        data=test_data,
        content_type='text/csv',
    )

    request_data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert request_data == 2