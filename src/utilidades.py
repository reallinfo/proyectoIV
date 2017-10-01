import platform
import os
import datetime

# Lanza el comando para limpiar la pantalla acorde al sistema operativo que se use
def limpiar_pantalla():
	sistema = platform.system()
	if sistema == 'Windows':
		basura = os.system('cls')
	elif sistema == 'Linux' or sistema == 'Darwin':
		basura = os.system('clear')
 
# Recibe como parámetro un objeto datetime y devuelve los valores que representa como un código AAAAMMDD:HHMM
def obtener_id(fecha):
	if type(fecha) is not datetime.datetime:
		raise RuntimeError("obtener_id acepta sólo datetime como parámetros.")

	if fecha.month < 10:
		mes = "0" + str(fecha.month)
	else:
		mes = str(fecha.month)

	if fecha.day < 10:
		dia = "0" + str(fecha.day)
	else:
		dia = str(fecha.day)

	if fecha.hour < 10:
		hora = "0" + str(fecha.hour)
	else:
		hora = str(fecha.hour)

	if fecha.minute < 10:
		minutos = "0" + str(fecha.minute)
	else:
		minutos = str(fecha.minute)

	res = str(fecha.year) + mes + dia + ":" + hora + minutos

	return res

# Recibe como argumento un string con formato ID AAAAMMDD:HHMM y devuelve una fecha con esos datos.
def obtener_fecha(id):
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
