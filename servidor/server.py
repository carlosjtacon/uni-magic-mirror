import bottle, json
from random import randint
from bottle import route, run, request

# variable global diccionario (dict) 
# que contiene la respuesta a devolver
respuesta = {
    'status': 0,
    'sensors': {
        'temperature': 0,
        'humidity': 0
    }
}

# ruta a la que el cliente hará peticiones
@route('/status', methods='GET OPTIONS'.split())
def getStatus():
    """Este método devolverá un json comprensible para el cliente 
    con un objeto global status que debemos crear"""
    bottle.response.set_header("Access-Control-Allow-Origin", "*")
    bottle.response.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    bottle.response.set_header("Access-Control-Allow-Headers", "Origin, Content-Type")

    # forma de actualizar la variable global de respuesta
    # se tendrá que hacer igual desde el POST y eliminar estas líneas
    status = { 'status': randint(0, 5) }
    respuesta.update(status)
    
    return respuesta


# ruta a la que hey-athena enviará datos
@route('/athena', method='POST')
def postAthena():
    """Athena enviará datos a esta url, esos datos modificarán el 
    objeto status que se devolverá en la petición getStatus()"""

    req.body
    
    


run(host = 'localhost', port = '8000', debug = True)
