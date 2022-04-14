'''
Registrar user 0 tokens
Cada user recebe 10 tokens
post de sentença - 1 token
get do db - 1 token
'''
from flask import Flask,render_template
from flask_restful import Api 
from models.resources.register import Register

app = Flask(__name__)
api =  Api(app)
 
title = "Flask tutorial"
subtitle = "Running on port 5000"




'''
 ***********************
 *       API ROUTES    *
 ***********************
'''
api.add_resource(Register, '/register')

'''
***********************
*       APP ROUTES    *
***********************
'''
@app.route('/')
def hello_world():
  return render_template('index.html', title=title, subtitle=subtitle)



# from flask import Flask,render_template
# from flask_restful import Api
# from models.resources.calculations import Add, Subtract, Multi, Divide
# app = Flask(__name__)
# api =  Api(app)
# 
# title = "Flask tutorial"
# subtitle = "Running on port 5000"
# 
# '''
# ***********************
# *       API ROUTES    *
# ***********************
# '''
# api.add_resource(Add, "/add")
# api.add_resource(Subtract, "/minus")
# api.add_resource(Multi, "/multi")
# api.add_resource(Divide, "/div")
# #----------------------------------'''
# 
# '''
# ***********************
# *       APP ROUTES    *
# ***********************
# '''
# @app.route('/')
# def hello_world():
#   return render_template('index.html', title=title, subtitle=subtitle)
# 
# @app.route('/teste')
# def test():
#   return "teste"
# #--------------------------------------------------------------------'''
# 
# if __name__ == '__main__':
#   app.run(debug=True)