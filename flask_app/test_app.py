import pytest
import app
import requests
import time

def test_website_up():
    assert requests.get("http://localhost:5000").status_code == 200, "the website is not up"

def test_get_mean():
    assert app.get_mean("1,2,3,4") == 2.5, "the mean function isn't working properly"

def test_stress_test():
    start_time = time.time()
    url_list=["http://localhost:5000"]*1000
    for url in url_list:
        requests.get(url)
    assert (time.time()-start_time)/1000 < 0.1, "the website is too slow"