from flask import Flask, request, Response, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_swagger import swagger

import uuid
import datetime
# import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# class Task:
#
#     def __init__(self, name, priority, description):
#         self.uuid = str(uuid.uuid1())
#         self.name = name
#         self.priority = priority
#         self.description = description
#         self.creation_date = datetime.datetime.now().strftime("%H:%M:%S")
#         self.last_update = datetime.datetime.now().strftime("%H:%M:%S")
#
#
#     def __dict__(self):
#         return {
#             "uuid": self.uuid,
#             "name": self.name,
#             "creation_date" : self.creation_date,
#             "last_update" : self.last_update,
#             "description" : self.description,
#             "priority" : self.priority
#         }
#
# list_task = []
