#!/usr/bin/python3

import sys
sys.path.append(".") # to be able to import packages from parent directory
from prometheus_client import start_http_server
import flask
from flask import request, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
ma = Marshmallow(app)

from backend.pinger.pingWorker import startWorker
from backend.models.target import Target, targets_schema

@app.route('/api/v1/targets/start', methods=['POST'])
def targetsStart():
    print('Starting ping worker on target: ' + request.json['host'])
    startWorker(request.json['host'])
    resp = jsonify(success=True)
    return resp

@app.route('/api/v1/targets/list', methods=['GET'])
def targetsList():
    newTarget = Target()
    newTarget.id = "1"
    newTarget.host = "google.com"
    newTarget.interval = 1000

    newTarget2 = Target()
    newTarget2.id = "2"
    newTarget2.host = "test.com"
    newTarget2.interval = 3000

    targets = [newTarget, newTarget2]
    result = targets_schema.dump(targets)
    print(targets)
    return jsonify(result)

@app.before_first_request
def initialize():
    # Start up the server to expose the metrics.
    print("Start serving metrics...")
    start_http_server(8001) #8001

# Start up the api server
print("Starting API...")
app.run(host='0.0.0.0', port=8000) #8000