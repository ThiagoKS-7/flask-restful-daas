from pymongo import MongoClient
from flask_restful import Resource
from flask import request
from repositories.requests import handleRequest

# instanciando mongoClient na porta default
client = MongoClient("localhost", 27017)
# novo database de nome SentencesDatabase
db = client.SentencesDatabase
# nova colecttion de nome Users
Users = db.Users

#criar resource
class Register(Resource):
  def post(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'register')
    return res

class Store(Resource):
  def post(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'store')
    return res