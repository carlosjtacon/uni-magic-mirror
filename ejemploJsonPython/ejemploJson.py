#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def leerArchivo(directorio):
    #leemos el archivo sin mas
    archivo = open(directorio, "r")
    return archivo.read()


#print leerArchivo("datos.json")

def codificarJson(directorio):
    datos = leerArchivo(directorio)
    #podemos imprimirlo directamente como datos nativos
    print "Datos nativos: ", datos
    #no se por que pero si no importo json va todo bien
    #cuado lo importo hace los prints dos veces
    #¿alguien sabe algo?
    datosString = json.dumps(datos)
    print "Datos JSON: ", datosString

def decodificarJson(directorio):
    datos = leerArchivo(directorio)
    datosDecodificados = json.loads(datos)
    print "Decodificado: ", datosDecodificados
    

codificarJson("datos.json")
#decodificarJson("datos.json")
