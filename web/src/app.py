'''
Registrar user 0 tokens
Cada user recebe 10 tokens
post de sentença - 1 token
get do db - 1 token
'''
from flask import Flask,render_template
from flask_restful import Api 
from web.src.models.resources.manage_sentence import Register, Store

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
api.add_resource(Store, '/store')

'''
***********************
*       APP ROUTES    *
***********************
'''
@app.route('/')
def hello_world():
  return render_template('index.html', title=title, subtitle=subtitle)


if __name__ == '__main__':
  app.run(debug=True)

