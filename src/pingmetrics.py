#!/usr/bin/python3

from pythonping import ping
from prometheus_client import start_http_server, Histogram
import setInterval 

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

def pingTarget1():
    doOnePing('192.168.0.2')

if __name__ == '__main__':
    h = Histogram('ping_latency_miliseconds', 'Time it takes to get a ping reponse for target')
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    setInterval.setInterval(0.5,pingTarget1)