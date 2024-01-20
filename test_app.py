import app
import json
import warnings

def test_name():
    response = app.app.test_client().get('/name')
    assert response.status_code == 200
    assert response.data == b'Atharva'

def test_age():
    response = app.app.test_client().get('/age')
    assert response.status_code == 404
    assert response.data == b'41'

