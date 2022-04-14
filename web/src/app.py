from flask import Flask,render_template
from flask_restful import Api
from models.resources.calculations import Add, Subtract, Multi, Divide
from models.resources.visit import Visit

# instanciando app flask
app = Flask(__name__)
# instanciando api flask-restful
api =  Api(app)

# declaracao de vars
title = "Flask tutorial"
subtitle = "Running on port 5000"
teste = "Teste"

'''
***********************
*       API ROUTES    *
***********************
'''
# add_resource - inclui rota
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/minus")
api.add_resource(Multi, "/multi")
api.add_resource(Divide, "/div")
api.add_resource(Visit, "/hello")
#----------------------------------'''

'''
***********************
*       APP ROUTES    *
***********************
'''
@app.route('/')
def hello_world():
  return render_template('index.html', title=title, subtitle=subtitle)

@app.route('/teste')
def test():
  return render_template('test.html', title=title, teste=teste)
#--------------------------------------------------------------------'''

if __name__ == '__main__':
  app.run(host='0.0.0.0')