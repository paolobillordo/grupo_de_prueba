from flask import Flask, request
from config import Config
from funciones import Func


def init_app():
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)

    @app.route('/')
    def hello_world():
        return 'Bienvenido al ejercicio 1'
    
    @app.route('/info')
    def mostrar_bienvenida():
        return 'Bienvenido a ' + Config.APP_NAME
    
    @app.route('/about')
    def about():
        return Func.about()

    @app.route('/sum/<int:num1>/<int:num2>')
    def suma_2_num(num1, num2):
        return f'La suma es {num1 + num2}'

    @app.route('/age/<dob>')
    def cumple(dob):           
        return Func.cumple(dob)

    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operate(operation,num1, num2):
        return Func.operate(operation,num1, num2)
    
    @app.route('/operate')
    def operate2():
        operation = request.args.get('operation')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return Func.operate(operation, num1, num2)

        









    return app