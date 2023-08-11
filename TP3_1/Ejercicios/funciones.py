from flask import jsonify
from config import Config
from datetime import datetime,timedelta
from math import trunc

class Func:

    def about():
        Info={
            "appname" : Config.APP_NAME,
            "description" :Config.DESCRIPTION,
            "developers" :Config.DEVELOPERS,
            "version" : Config.VERSION
            }        
        return jsonify(Info)
    
    def cumple(dob):       
        edad = (datetime.today() - datetime.strptime(dob, '%Y-%m-%d')) / timedelta(days=365)
        if (edad <= 0):
            return jsonify("La fecha no es válida. Ingrese una fecha anterior a la actual.")   
        return f'Tu edad es {trunc(int(edad))} años'
    
    def operate(operation,num1, num2):
        if (operation == "sum"):
            return f'La suma entre {num1} y {num2} es: {num1 + num2}'
        elif (operation == "sub"):
            return f'La resta entre {num1} y {num2} es: {num1 - num2}'
        elif (operation == "mult"):
            return f'La multiplicación entre {num1} y {num2} es: {num1 * num2}'
        elif (operation == "div"):
            if (num2 == 0):
                return "No esta definida la división por 0"
            return f'La división entre {num1} y {num2} es: {num1 / num2}'
        return "No existe ruta para ese endpoint"
    
    
    