#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import bottle
from bottle import Bottle, route, run, request
from random import randint

#ejemplo basico de get
@route('/index')
def hola():
    return "<h1>HOLA CAPULLOS</h1>"

#ejemplo de urls dinamicas
@route('/')
@route('/index/<nombre>')
def rutasDinamicas(nombre = None):
    #para ver como funciona este ejemplo prueba a poner
    #127.0.0.1:8000/index/"elnombrequetuquierassincomillas"
    return 'Hola %r, ¿que coño quieres?' %nombre

#ejemplo de envio de un post
@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>'''

#ejemplo práctico de login form
@route('/login', method='POST')
def do_login():
    usuario = request.forms.get('username')
    clave = request.forms.get('password')
    if usuario == "1234" and clave == "1234":
        return "<p><b>Los datos son correctos. Eres de los nuestros</b></p>"
    else:
        return "<p><b>FUERA DE AQUÍ %r INTRUSO. TUS DATOS NO SON CORRECTOS</b></p>"%usuario

#ejemplo de json
@route('/json')
def ejemplo():
    data = request.json
    #todavia no se que hacer con el json cuando probemos con uno de verdad veremos como funciona
    print data

#ejemplo json post
@route('/json', method='POST')
def postJson():
    datos = request.json
    #igual que antes: todavía no se qué debo hacer con el json, pero con esto lo recibimos


#ruta a la que el cliente hará peticiones
@route('/status', methods='GET OPTIONS'.split())
def getStatus():
    """Este método devolverá un json comprensible para el cliente 
    con un objeto global status que debemos crear"""
    bottle.response.set_header("Access-Control-Allow-Origin", "*")
    bottle.response.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    bottle.response.set_header("Access-Control-Allow-Headers", "Origin, Content-Type")

    status = randint(0, 5)
    response = {
        'status': status,
        'sensors': {
            'temperature': 35,
            'humidity': 10
            }
        }
    return response


#ruta a la que hey-athena enviará datos
@route('/athena', method='POST')
def postAthena():
    """Athena enviará datos a esta url, esos datos modificarán el 
    objeto status que se devolverá en la petición getStatus()"""
    


run(host = 'localhost', port = '8000', debug = True)
