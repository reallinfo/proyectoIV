
from datetime import *


##########################
### GESTIÓN DE FECHAS ###
########################

# Devuelve datetime de ayer. */- extra horas.
def ayer(extra = 0):
	try:
		int(extra)
	except:
		extra = 0
		print("El argumento de ayer() debe ser un entero válido. Ejecutando ayer(0)")
	return datetime.today() - timedelta(days = 1, hours = extra)

# Devuelve datetime de hoy. */- extra horas.
def hoy(extra = 0):
	try:
		int(extra)
	except:
		extra = 0
		print("El argumento de hoy() debe ser un entero válido. Ejecutando hoy(0)")
	return datetime.today() + timedelta(hours = extra)

# Devuelve datetime de mañana. */- extra horas.
def manana(extra = 0):
	try:
		int(extra)
	except:
		extra = 0
		print("El argumento de manana() debe ser un entero válido. Ejecutando manana(0)")
	return datetime.today() + timedelta(days = 1, hours = extra)

# Recibe un datetime. Devuelve True si la fecha es anterior a hoy.
def fecha_pasada(fecha):
	if type(fecha) is not datetime:
		raise TypeError("fecha_pasada sólo admite datetime como argumento.")
	if fecha > hoy():
		return False
	else:
		return True

# Recibe como parámetro tres datetime. Devuelve true si la primera se encuentra entre las otras dos.
def fecha_entre(fecha, antes, despues):
	if type(fecha) is not datetime or type(antes) is not datetime or type(despues) is not datetime:
		raise TypeError("fecha_entre() sólo admite datetime como argumentos")
	if fecha > antes and fecha < despues:
		return True
	else:
		return False


########################
### CONTROL DE HORAS ###
########################

# Recibe un datetime como parámetro. Devuelve True si aún no ha pasado.
def hora_pasada(hora):
	if type(hora) is not datetime:
		raise TypeError("hora_pasada sólo admite datetime como argumento")
	if hora < datetime.now():
		return True
	else:
		return False
