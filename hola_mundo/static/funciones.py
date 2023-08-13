from flask import jsonify, request
from config import Config
from datetime import datetime,timedelta
from math import trunc
import json
from hola_mundo.static.stack import *


# Ejercicio 3
def fun_about():
    info={
        "appname" : Config.APP_NAME,
        "description" :Config.DESCRIPTION,
        "developers" :Config.DEVELOPERS,
        "version" : Config.VERSION
        }        
    return (info, 200, {'Content-Type':'application/json'})
    
# Ejercicio 5    
def func_cumple(dob):       
    edad = (datetime.today() - datetime.strptime(dob, '%Y-%m-%d')) / timedelta(days=365)
    if (edad < 0):
        return -1   
    return int(edad)
    
# Ejercicio 6 y 7
def func_operate(operation,num1, num2):    
    if (operation == "sum"):
        return ({'respuesta': f'La suma entre {num1} y {num2} es: {num1 + num2}'}, 200, {'Content-Type':'application/json'})
    elif (operation == "sub"):
        return ({'respuesta': f'La resta entre {num1} y {num2} es: {num1 - num2}'}, 200, {'Content-Type':'application/json'})
    elif (operation == "mult"):
        return ({'respuesta': f'La multiplicación entre {num1} y {num2} es: {num1 * num2}'}, 200, {'Content-Type':'application/json'})
    elif (operation == "div"):
        if (num2 == 0):
            return ({'error': "No esta definida la división por 0"}, 400, {'Content-Type':'application/json'})
        return ({'respuesta': f'La división entre {num1} y {num2} es: {num1 / num2}'}, 200, {'Content-Type':'application/json'})
    return ({'error': "No existe ruta para ese endpoint"}, 400, {'Content-Type':'application/json'})

# Ejercicio 8    
def func_title(word):
    titulo = word.title()
    respuesta = {
        "formatted_word": titulo
    }
    return (respuesta, 200, {'Content-Type':'application/json'})

# Ejercicio 9    
def func_documento(dni):
    numero_str = dni.replace(".","").replace("-","")
    for n in numero_str:
        if(n.isalpha()):
            return ({'error': "El DNI no debe contener letras"}, 400, {'Content-Type':'application/json'})
    if (numero_str[0] == "0" or len(numero_str) != 8):
        return ({'error': "El número de documento no es válido"}, 400, {'Content-Type':'application/json'})
    numero = int(numero_str)
    num_format = {
        "formatted_dni": numero
    }
    return (num_format, 200, {'Content-Type':'application/json'})

# Ejercicio 10    
def func_usuario():
    firstname = request.args.get('firstname').title()
    lastname = request.args.get('lastname').title()
    dob = request.args.get('dob')
    dni = request.args.get('dni')
    if(firstname == "" or lastname == "" or dob == "" or dni == ""):
        return ({'error': "Faltan datos"}, 400, {'Content-Type':'application/json'})        
    dni_tup = func_documento(dni)        
    if dni_tup[1] == 400:
        return (dni_tup)            
    edad = func_cumple(dob)
    if (edad == 0):
        return ({'error': "La fecha no es válida. Ingrese una fecha anterior a la actual."},400, {'Content-Type':'application/json'})        
    user = {
        "firstname": firstname,
        "lastname": lastname,
        "age": edad,
        "dni": dni_tup[0]['formatted_dni']
    }
    return (user, 200, {'Content-Type':'application/json'})

# Ejercicio 11        
def func_encode(keyword):
    cadena = keyword.upper().replace("+", " ")
    if (cadena[0] == " " or len(cadena) > 100):
        return ({'error': "Ingrese una clave válida, solo letras y numeros sin espacios al comienzo y signo + para separar palabras"}, 400, {'Content-Type':'application/json'})
    codigo = []
    with open('./hola_mundo/static/morse_code.json', 'r') as f:
        lette = json.load(f)['letters']
    for n in cadena:
        if (n in lette):
            codigo.append(lette[n])
        else:
            return ({'error': "Ingrese una clave válida, solo letras y numeros sin espacios al comienzo y signo + para separar palabras"}, 400, {'Content-Type':'application/json'})
    return ("+".join(codigo))

# Ejercicio 12    
def func_decode(morse_code):
    codigo = morse_code.split("+")
    mensaje = []
    with open('./hola_mundo/static/morse_code.json', 'r') as f:
        letters = json.load(f)['letters']
    for n in codigo:
        for clave in letters:
            if(n == letters[clave]):                    
                    mensaje.append(clave)
                            
    return (("".join(mensaje).capitalize()),200, {'Content-Type':'application/json'})
    
# Ejercicio 13
def func_convert(num):
    numero_decimal = 0
    for posicion, digito_string in enumerate(num[::-1]):
        if digito_string not in '01':
            return ({'error': "No es un número binario"}, 400, {'Content-Type':'application/json'})
        numero_decimal += int(digito_string) * 2 ** posicion
    return ({'numero decimal': numero_decimal}, 200,{'Content-Type':'application/json'})

# Ejercicio 14
def func_balance(input):
    stack = Stack()
    limiters = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for character in input:
        if character in '([{':
            stack.push(character)
        elif character in ')]}':
            if stack.is_empty() or stack.top() != limiters[character]:
                return ({'balanced': False}, 200, {'Content-Type':'application/json'})
            stack.pop()
    resultado = {
        "balanced": stack.is_empty()
    }
    return (resultado, 200, {'Content-Type':'application/json'})

