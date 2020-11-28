#!/usr/bin/python3

from pythonping import ping
from prometheus_client import start_http_server, Histogram
from backend.pinger.setInterval import setInterval

target = ''
h = Histogram('ping_latency_miliseconds', 'Time it takes to get a ping reponse for target')

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def doOnePing(target):
    responseList = ping(target, count=1)

    for response in responseList:
        h.observe(response.time_elapsed_ms)
        print(response.time_elapsed_ms)

def pingTarget():
    doOnePing(target)

def startWorker(host):
    target = host
    # Generate some requests.
    setInterval(0.5, pingTarget)