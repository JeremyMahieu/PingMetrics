#!/usr/bin/python3

import sys
sys.path.append(".") # to be able to import packages from parent directory
from prometheus_client import start_http_server
import flask
from flask import request, jsonify
from flask_cors import CORS
from backend.pinger.pingWorker import startWorker

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

@app.route('/api/v1/targets/start', methods=['POST'])
def targetsStart():
    print('Starting ping worker on target: ' + request.json['host'])
    startWorker(request.json['host'])
    resp = jsonify(success=True)
    return resp

# Start up the server to expose the metrics.
print("Start serving metrics...")
start_http_server(8001) 

# Start up the api server
print("Starting API...")
app.run(host='0.0.0.0', port=8000)