from flask import jsonify, request
from config import Config
from datetime import datetime,timedelta
from math import trunc
import json

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
        return (respuesta, 200, {'Content-Type':'application/json'})
    
    def documento(dni):
        numero_str = dni.replace(".","").replace("-","")
        for n in numero_str:
            if(n.isalpha()):
                return ("El DNI no debe contener letras", 400)
        if (numero_str[0] == "0" or len(numero_str) != 8):
            return ("El número de documento no es válido", 400)
        numero = int(numero_str)
        num_format = {
            "formatted_dni": numero
        }
        return (num_format, 200, {'Content-Type':'application/json'})
    
    def usuario():
        firstname = request.args.get('firstname').title()
        lastname = request.args.get('lastname').title()
        dob = request.args.get('dob')
        dni = request.args.get('dni')
        if(firstname == "" or lastname == "" or dob == "" or dni == ""):
            return ("Faltan datos", 400)
        numero_str = dni.replace(".","").replace("-","")
        for n in numero_str:
            if(n.isalpha()):
                return ("El DNI no debe contener letras", 400)
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
        return (user, 200, {'Content-Type':'application/json'})
        
    def encode(keyword):
        cadena = keyword.upper().replace("+", " ")
        if (cadena[0] == " " or len(cadena) > 100):
            return ("Ingrese una clave válida, solo letras y numeros sin espacios al comienzo y signo + para separar palabras", 400)
        codigo = []
        with open('morse_code.json', 'r') as f:
           lette = json.load(f)['letters']
        for n in cadena:
            if (n in lette):
                codigo.append(lette[n])
            else:
                return ("Ingrese una clave válida, solo letras y numeros sin espacios al comienzo y signo + para separar palabras", 400)
        return ("+".join(codigo))
    
    def decode(morse_code):
        codigo = morse_code.split("+")
        mensaje = []
        with open('morse_code.json', 'r') as f:
           letters = json.load(f)['letters']
        for n in codigo:
            for clave in letters:
                if(n == letters[clave]):                    
                    mensaje.append(clave)
                            
        return ("".join(mensaje).capitalize())
    
    
   