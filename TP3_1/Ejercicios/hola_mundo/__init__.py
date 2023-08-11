from flask import Flask,jsonify
from config import Config
from datetime import datetime,timedelta
from math import trunc


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
        Info={
            "appname" : Config.APP_NAME,
            "description" :Config.DESCRIPTION,
            "developers" :Config.DEVELOPERS,
            "version" : Config.VERSION
            }        
        return jsonify(Info)

    @app.route('/sum/<int:num1>/<int:num2>')
    def suma_2_num(num1, num2):
        return f'La suma es {num1 + num2}'

    @app.route('/age/<dob>')
    def cumple(dob):
        edad = (datetime.today() - datetime.strptime(dob, '%Y-%m-%d')) / timedelta(days=365)        
        return f'Tu edad es {trunc(int(edad))} años'

    







    return app