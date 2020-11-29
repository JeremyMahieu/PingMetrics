from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

class TargetSchema(ma.Schema):
    class Meta:
        fields = ('id','host','interval')

target_schema = TargetSchema()
targets_schema = TargetSchema(many=True)

class Target:
    id = ''
    host = ''
    interval = 0