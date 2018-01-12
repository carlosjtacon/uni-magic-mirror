import requests, json

try:

    ## PARA SIMULAR UNA PETICIÓN DE 
    ## COMANDO DE VOZ CAMBIAR STATUS
    ## STATUS PARA ATHENA:
    ##   4: CLIMA
    ##   5: ALERTAS / NOTICIAS IMPORTANTES
    ##   6: BITCOIN
    payload_athena = { 'status': 4 }
    requests.post("http://localhost:8000/athena", json=json.dumps(payload_athena))
    

    ## PARA SIMULAR UNA PETICIÓN DE ARDUINO 
    ## MODIFICAR LOS VALORES DE LOS SENSORES
    payload_arduino = {
        'sensors': {
            'temperature': '36.00',
            'humidity': '23.00',
            'presence': '1',
            'pulsadorCepillo': '0',
            'pulsadorAgua':'0'
        }
    }
    requests.post("http://localhost:8000/arduino", json=json.dumps(payload_arduino))

except ValueError:
    print("Algo no funcionó" + ValueError)
