import requests, json
import serial

ser = serial.Serial('/dev/cu.usbmodem411', 9600)
while True:
	try:
		#datos = '36.00,23.00,73.40,1'
		datos = str(ser.readline())[+2:-3]
		print(datos)
		sensores = datos.split(',')
		# para athena payload = { 'status': numero } y el resto igual
		payload = {
			'sensors': {
				'humidity': sensores[0],
				'temperature': sensores[1],
				#'temperatureF': sensores[2],
				'presence': sensores[3],
				'pulsadorCepillo': sensores[4],
				'pulsadorAgua':sensores[5]
			}
		}

		requests.post("http://localhost:8000/arduino", json=json.dumps(payload))
	except ValueError:
		print("Algo no funciono" + ValueError)