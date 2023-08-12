from flask import Flask, request, jsonify
from config import Config
from funciones import Func
from datetime import datetime,timedelta




def init_app():
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
#Ejercicio 1
    @app.route('/')
    def hello_world():
        return 'Bienvenido al ejercicio 1'
#Ejercicio 2   
    @app.route('/info')
    def mostrar_bienvenida():
        return 'Bienvenido a ' + Config.APP_NAME
#Ejercicio 3    
    @app.route('/about')
    def about():
        return Func.about()
#Ejercicio 4
    @app.route('/sum/<int:num1>/<int:num2>')
    def suma_2_num(num1, num2):
        return f'La suma es {num1 + num2}'
#Ejercicio 5
    @app.route('/age/<dob>')
    def cumple(dob):           
        return Func.cumple(dob)
#Ejercicio 6
    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operate(operation,num1, num2):
        return Func.operate(operation,num1, num2)
#Ejercicio 7    
    @app.route('/operate')
    def operate2():
        operation = request.args.get('operation')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return Func.operate(operation, num1, num2)
#Ejercicio 8    
    @app.route('/title/<string:word>')
    def title_0(word):
        return Func.title_1(word)
#Ejercicio 9    
    @app.route('/formatted/<string:dni>')
    def documento(dni):        
        return Func.documento(dni)
#Ejercicio 10    
    @app.route('/format')
    def usuario():
        return Func.usuario()
#Ejercicio 11    
    @app.route('/encode/<string:keyword>')
    def encode(keyword):
        return Func.encode(keyword)
#Ejercicio 12
    @app.route('/decode/<string:morse_code>')
    def decode(morse_code):
        return Func.decode(morse_code)
    
    







    return app