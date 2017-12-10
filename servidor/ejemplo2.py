#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from bottle import Bottle, route, run, request

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
@route('/json/')
def ejemplo():
    data = request.json
    print data

run(host = 'localhost', port = '8000', debug = True)
