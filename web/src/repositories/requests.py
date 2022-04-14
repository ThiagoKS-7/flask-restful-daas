from flask import request


def checkPostedData(body, functionName):
  # checa se um dos dois parametros ñ tá no body
  if 'x' not in body or 'y' not in body:
    error = {
      "message": "Error: missing required parameter.",
      "status": 301
    }
    return error
  # Ifs encadeados pra checar qual função é
  if functionName == 'add':
      x = int(body['x'])
      y = int(body['y'])
      add = x + y
      res = {
        "message": add,
        "status": 200
      }
      return res
  elif functionName == 'minus':
      x = int(body['x'])
      y = int(body['y'])
      subtract = x - y
      res = {
        "message": subtract,
        "status": 200
      }
      return res
  elif functionName == 'multi':
      x = int(body['x'])
      y = int(body['y'])
      multiplication = x * y
      res = {
        "message": multiplication,
        "status": 200
      }
      return res
  elif functionName == 'div':
    if body['y'] == 0:
      error = {
      "message": "Error: division by zero.",
      "status": 302
      }
    else:
      x = int(body['x'])
      y = int(body['y'])
      division = x / y
      res = {
        "message": division,
        "status": 200
      }
      return res
# tenta checar se a request tá certa
# se não der, retorna bad request
def handleRequest(body, routeName):
    try:  
      res = checkPostedData(body, routeName)
      return res
    except request .HTTP_error as exception:
      error = {
        "message": exception,
        "status": 400
      }
      return error