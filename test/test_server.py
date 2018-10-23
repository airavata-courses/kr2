import pytest
import server
import os
import json


def test_initial():
    test_app = server.app
    test_client = test_app.test_client()
    test_app.testing = True
    init = test_client.get('/jobs/testing')
    # print(init)
    assert b"US Naukri" in init.data


def test_job():

    # Test if we are able to get jobs
    test_app = server.app
    test_client = test_app.test_client()
    test_app.testing = True
    headers_content_form_data = {'Content-Type': 'multipart/form-data'}
    jobs = test_client.post('/jobs/total',headers=headers_content_form_data,
        data={'desc': 'node','jobType':'true'})
    data = json.loads(jobs.get_data(as_text=True))
    #checking for response code
    assert jobs.status_code == 200
    	
def test_parameters():

    test_app = server.app
    test_client = test_app.test_client()
    test_app.testing=True
    headers_content_form_data = {'Content-Type': 'multipart/form-data'}
    response = test_client.post('/job',headers=headers_content_form_data,
        data={'desc': 'java','jobType': 'AnythingButTrueOrFalse', 'email': 'kr2@kr2.com'})

    resText = json.loads(response.get_data(as_text=True))

    assert resText['error']=="jobType not passed as true/false" 
    assert response.status_code == 400
