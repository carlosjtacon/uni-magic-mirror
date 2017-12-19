import requests, json

try:
    datos = '36.00,23.00,73.40,1'

    sensores = datos.split(',')
    # para athena payload = { 'status': numero } y el resto igual
    payload = {
        'sensors': {
            'temperature': sensores[0],
            'humidity': sensores[1],
            'presence': sensores[3],
            'pulsadorCepillo': '0',
            'pulsadorAgua':'0'
        }
    }

    requests.post("http://localhost:8000/arduino", json=json.dumps(payload))
except ValueError:
    print("Algo no funciono" + ValueError)
