from flask import jsonify, request
from config import Config
from datetime import datetime,timedelta
from math import trunc
from morse_code import letters

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
    
    def title_1(word):
        titulo = word.title()
        respuesta = {
            "formatted_word": titulo
        }
        return jsonify(respuesta)
    
    def documento(dni):
        numero_str = dni.replace(".","").replace("-","")
        numero = int(numero_str)
        num_format = {
            "formatted_dni": numero
        }
        if (numero_str[0] == "0" or len(numero_str) != 8):
            return ("El número de documento no es válido", 400)
        return jsonify(num_format)
    
    def usuario():
        firstname = request.args.get('firstname').title()
        lastname = request.args.get('lastname').title()
        dob = request.args.get('dob')
        dni = request.args.get('dni')
        numero_str = dni.replace(".","").replace("-","")
        numero = int(numero_str)        
        if (numero_str[0] == "0" or len(numero_str) != 8):
            return ("El número de documento no es válido", 400)
        edad = int((datetime.today() - datetime.strptime(dob, '%Y-%m-%d')) / timedelta(days=365))
        if (edad <= 0):
            return jsonify("La fecha no es válida. Ingrese una fecha anterior a la actual.")        
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "age": edad,
            "dni": numero
        }
        return jsonify(user)
    
    def encode(keyword):
        cadena = keyword.upper()
        codigo = []
        for n in cadena:
            if (n in letters):
                codigo.append(letters[n])        
        return ("+".join(codigo))
    