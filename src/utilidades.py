import platform
import os
import datetime

def limpiar_pantalla():
	sistema = platform.system()
	if sistema == 'Windows':
		basura = os.system('cls')
	elif sistema == 'Linux' or sistema == 'Darwin':
		basura = os.system('clear')

def obtener_id(fecha):
	if type(fecha) is not datetime:
		raise RuntimeError("obtener_id acepta sólo datetime como parámetros.")
	res = str(fecha.year) + str(fecha.month) + str(fecha.day) + ":" + str(fecha.hour) + str(fecha.minute)
	return res

def obtener_fecha(id):
	try:
		
	except:
		print("Error al pasar de id a fecha")
