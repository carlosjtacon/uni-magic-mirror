import requests
import serial

ser = serial.Serial('COM4', 9600)
while True:
	datos = str(ser.readline())
	print(datos[+2:-3])
	try:
		datos = str(ser.readline())[+2:-3]
		print(datos)
		r = requests.post("http://localhost:8000/", data={'sensor': datos})
	except ValueError:
		print ("Algo no funciono" + ValueError)