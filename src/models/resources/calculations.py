from flask import request
from flask_restful import Resource
from repositories.requests import handleRequest

class Add(Resource):
  def post(self):
    body = request.get_json()

    if body:
      res = handleRequest(body, 'add')
      return res

class Subtract(Resource):
  def post(self):
    body = request.get_json()

    if body:
     res = handleRequest(body, 'minus')
     return res

class Multi(Resource):
  def post(self):
    body = request.get_json()

    if body:
     res = handleRequest(body, 'multi')
     return res

class Divide(Resource):
  def post(self):
    body = request.get_json()

    if body:
     res = handleRequest(body, 'div')
     return res