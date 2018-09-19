"""
Gestión de fechas con funciones que serán útiles a la hora de trabajar con la base de datos del proyecto. Trabaja tanto con fechas como con horas.
"""


from datetime import *
import warnings


##########################
### GESTIÓN DE FECHAS ###
########################

def ayer(extra = 0):
	""" Devuelve datetime de ayer. */- extra horas. """
	try:
		int(extra)
	except:
		extra = 0
		warnings.warn("El argumento de ayer() debe ser un entero válido. Ejecutando ayer(0)", UserWarning)
	return datetime.today() - timedelta(days = 1, hours = extra)

def hoy(extra = 0):
	""" Devuelve datetime de hoy. */- extra horas. """
	try:
		int(extra)
	except:
		extra = 0
		warnings.warn("El argumento de hoy() debe ser un entero válido. Ejecutando hoy(0)", UserWarning)
	return datetime.today() + timedelta(hours = extra)

def manana(extra = 0):
	""" Devuelve datetime de mañana. */- extra horas."""
	try:
		int(extra)
	except:
		extra = 0
		warnings.warn("El argumento de manana() debe ser un entero válido. Ejecutando manana(0)")
	return datetime.today() + timedelta(days = 1, hours = extra)

def fecha_pasada(fecha):
	""" Recibe un datetime. Devuelve True si la fecha es anterior a hoy."""
	if type(fecha) is not datetime:
		raise TypeError("fecha_pasada sólo admite datetime como argumento.")

	if fecha > hoy():
		return False
	else:
		return True

def fecha_entre(fecha, antes, despues):
	""" Recibe como parámetro tres datetime. Devuelve true si la primera se encuentra entre las otras dos."""
	if type(fecha) is not datetime or type(antes) is not datetime or type(despues) is not datetime:
		raise TypeError("fecha_entre() sólo admite datetime como argumentos")
	if fecha > antes and fecha < despues:
		return True
	else:
		return False


########################
### CONTROL DE HORAS ###
########################

def hora_pasada(hora):
	""" Recibe un datetime como parámetro. Devuelve True si aún no ha pasado."""
	if type(hora) is not datetime:
		raise TypeError("hora_pasada sólo admite datetime como argumento")
	if hora < datetime.now():
		return True
	else:
		return False
