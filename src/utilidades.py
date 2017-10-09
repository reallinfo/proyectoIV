"""
Módulo de utilidades varias para gestionar los diferentes códigos manejados por la base de datos así como la interacción con el sistema operativo que use el programa.
"""


import platform
import os
import datetime

def limpiar_pantalla():
	""" Lanza el comando para limpiar la pantalla acorde al sistema operativo que se use. """
	sistema = platform.system()
	if sistema == 'Windows':
		basura = os.system('cls')
	elif sistema == 'Linux' or sistema == 'Darwin':
		basura = os.system('clear')

def pausa_ejecucion():
	""" Pausa la ejecución hasta que se pulse alguna tecla. """
	sistema = platform.system()
	if sistema == 'Windows':
		basura = os.system('pause')

def plataforma():
	""" Devuelve el sistema operativo sobre el que corre el programa."""
	return platform.system()

def obtener_fecha(id):
	""" Recibe como argumento un string con formato ID AAAAMMDD:HHMM y devuelve una fecha con esos datos. """
	try:
		if type(id) is not str:
			raise RuntimeError

		ano = id[0] + id[1] + id[2] + id[3]
		mes = id[4] + id[5]
		dia = id[6] + id[7]
		hora = id[9] + id[10]
		minutos = id[11] + id[12]
		res = datetime.datetime(int(ano), int(mes), int(dia), int(hora), int(minutos))

		return res

	except:
		print("Error al pasar de id a fecha")

def obtener_cod_fecha(fecha):
	""" A partir de una fecha (datetime) devuelve el código AAAAMMDD"""
	try:
		if type(fecha) is not datetime.datetime:
			raise RuntimeError

		if fecha.month < 10:
			mes = "0" + str(fecha.month)
		else:
			mes = str(fecha.month)

		if fecha.day < 10:
			dia = "0" + str(fecha.day)
		else:
			dia = str(fecha.day)

		return str(fecha.year) + mes + dia

	except:
		print("obtener_cod_fecha() sólo admite datetime como parámetro")

def obtener_cod_hora(fecha):
	"""  A partir de una fecha (datetime) devuelve el código HHMM"""
	try:
		if type(fecha) is not datetime.datetime:
			raise RuntimeError

		if fecha.hour < 10:
			hora = "0" + str(fecha.hour)
		else:
			hora = str(fecha.hour)

		if fecha.minute < 10:
			minutos = "0" + str(fecha.minute)
		else:
			minutos = str(fecha.minute)

		return hora + minutos

	except:
		print("obtener_cod_hora() sólo admite datetime como parámetro")


def obtener_id(fecha):
	""" Recibe como parámetro un objeto datetime y devuelve los valores que representa como un código AAAAMMDD:HHMM. """
	if type(fecha) is not datetime.datetime:
		raise RuntimeError("obtener_id acepta sólo datetime como parámetros.")

	f = obtener_cod_fecha(fecha)
	h = obtener_cod_hora(fecha)
	return f + ":" + h

def obtener_ano(cod_fecha):
	""" A partir de un código fecha (AAAAMMDD) devuelve el año (AAAA). """
	return cod_fecha[0] + cod_fecha[1] + cod_fecha[2] + cod_fecha[3]

def obtener_mes(cod_fecha):
	""" A partir de un código fecha (AAAAMMDD) devuelve el mes (MM). """
	return  cod_fecha[4] + cod_fecha[5]

def obtener_dia(cod_fecha):
	""" A partir de un código fecha (AAAAMMDD) devuelve el día (DD). """
	return cod_fecha[6] + cod_fecha[7]
