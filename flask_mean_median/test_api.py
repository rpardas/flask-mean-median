import pytest
from flask import json
from api import app

# Create a test client using the Flask application configured for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# test cases
test_data_json = json.dumps([1, 1, 2, 3, 5])
test_data_csv = '1,1,2,3,5'

# test and verify mean value
def test_mean(client):        
    response = client.post(
        '/stat/mean',
        data=test_data_json,
        content_type='application/json',
    )

    response_data = float(response.get_data(as_text=True))

    assert response.status_code == 200
    assert response_data == 2.4

# test and verify median value
def test_median(client):        
    response = client.post(
        '/stat/median',
        data=test_data_json,
        content_type='application/json',
    )

    response_data = float(response.get_data(as_text=True))

    assert response.status_code == 200
    assert response_data == 2