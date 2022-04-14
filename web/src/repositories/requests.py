import bcrypt
from flask import request


def checkPostedData(collection,body, functionName):
  # checa se um dos dois parametros ñ tá no body
  if 'username' not in body or 'password' not in body:
    error = {
      "message": "Error: missing required parameter usr/pwd.",
      "status": 301
    }
    return error
  # Ifs encadeados pra checar qual função é
  if functionName == 'register':
    usr = body["username"]
    pwd = body["password"].encode('utf-8')
    hash_pwd = bcrypt.hashpw(pwd, bcrypt.gensalt())
    have_same_data = collection.find_one({'Username': usr})
    if not have_same_data:
      collection.insert_one({
        "Username":usr,
        "Password":hash_pwd,
        "Tokens": 10
      })
      retJson = {
      "message":"You successfully signed up!",
      "status": 200
      }
    else:
      retJson = {
       "message":"Error! User already exists.",
       "status": 400
      }

    return retJson

# tenta checar se a request tá certa
# se não der, retorna bad request
def handleRequest(collection,body, routeName):
    try:  
      res = checkPostedData(collection,body, routeName)
      return res
    except request .HTTP_error as exception:
      error = {
        "message": exception,
        "status": 400
      }
      return error