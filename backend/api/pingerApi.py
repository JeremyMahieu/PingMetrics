#!/usr/bin/python3

import sys
sys.path.append(".")

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

app.run(host='0.0.0.0', port=8568)