import time
import redis
import requests
from flask import Flask, request
from prometheus_client import start_http_server

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
start_http_server(8010)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def get_mean(argument):
    if (argument == None):
        return "no list was given"
    argument_split = argument.split(",")
    argument_split = list(map(int, argument_split))
    mean = sum(argument_split)/len(argument_split)
    return mean


@app.route('/')
def home():
    argument = request.args.get("argument")
    return "hello to my sample flask app, I have been seen {} times\n If you want to calculate the mean add your numbers in the url like this : http://localhost:5000/?argument=1,2,3,4\nThe mean of your numbers in arguments is {}.\n".format(get_hit_count(), get_mean(argument))