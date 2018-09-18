import pytest
import app
import os
import json


def test_initial():
    test_app = app.job_info()
    test_client = test_app.test_client()
    test_app.testing = True
    init = test_client.get('/jobs/testing')
    print(init)
    assert "US Naukri" == init['result']

'''
def test_news():

    # Test if we are able to get news
    test_app = app.flask_news(os.environ["NEWS_API_KEY"])
    test_client = test_app.test_client()
    test_app.testing = True
    news = test_client.get('/top_headlines')
    data = json.loads(news.get_data(as_text=True))
    assert data["success"] == 1

    # Test if we are able to get error when token is wrong
    test_app = app.flask_news("wrong_token")
    test_client = test_app.test_client()
    test_app.testing = True
    news = test_client.get('/top_headlines')
    data = json.loads(news.get_data(as_text=True))
    assert data["success"] == 0
'''
