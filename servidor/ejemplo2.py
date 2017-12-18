#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import bottle
from bottle import Bottle, route, run, request
from random import randint

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
