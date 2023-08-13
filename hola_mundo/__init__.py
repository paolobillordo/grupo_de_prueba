from flask import Flask, request 
from hola_mundo.static.funciones import *

def init_app():
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)

#Ejercicio 1
    @app.route('/')
    def hello_world():
        return ('Bienvenido al ejercicio 1', 200, {'Content-Type':'application/json'})
    
#Ejercicio 2   
    @app.route('/info')
    def mostrar_bienvenida():
        return ('Bienvenido a ' + Config.APP_NAME, 200, {'Content-Type':'application/json'})
    
#Ejercicio 3
    @app.route('/about')
    def about():
        return fun_about()
    
#Ejercicio 4
    @app.route('/sum/<int:num1>/<int:num2>')
    def suma_2_num(num1, num2):
        return ({'suma': num1 + num2}, 200, {'Content-Type':'application/json'})
    
#Ejercicio 5
    @app.route('/age/<dob>')
    def cumple(dob):           
        edad = func_cumple(dob)
        print(edad)
        if  edad >= 0:
            return ({'edad': edad}, 200, {'Content-Type':'application/json'})
        else: 
            return ({'error': "La fecha no es válida. Ingrese una fecha anterior a la actual."}, 400, {'Content-Type':'application/json'})
        
#Ejercicio 6
    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operate(operation,num1, num2):
        return func_operate(operation,num1, num2)
    
#Ejercicio 7    
    @app.route('/operate')
    def operate2():
        operation = request.args.get('operation')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return func_operate(operation, num1, num2)
    
#Ejercicio 8    
    @app.route('/title/<string:word>')
    def title(word):
        return func_title(word)
    
#Ejercicio 9    
    @app.route('/formatted/<string:dni>')
    def documento(dni):        
        return func_documento(dni)
    
#Ejercicio 10    
    @app.route('/format')
    def usuario():
        return func_usuario()
    
#Ejercicio 11    
    @app.route('/encode/<string:keyword>')
    def encode(keyword):
        return func_encode(keyword)
    
#Ejercicio 12
    @app.route('/decode/<string:morse_code>')
    def decode(morse_code):
        return func_decode(morse_code)
    
#Ejercicio 13
    @app.route('/convert/binary/<string:num>')
    def convert(num):
        return func_convert(num)
    
#Ejercicio 14
    @app.route('/balance/<string:input>')
    def balance(input):
        return func_balance(input)

    return app