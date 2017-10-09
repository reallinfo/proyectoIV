"""
Programa con interfaz de usuario para probar las funcionalidades de gestion_reservas.

Está pensado sólo para hacer pruebas, por lo que a partir de cierto punto no se comprueban los tipos introducidos ni los errores.
"""

# Modificación del path para incluir las demás carpetas, por comodidad a la hora de importar.
import sys, platform
if platform.system is 'Windows':
	sys.path.append(".\src")
else:
	sys.path.append("./src")


import fechas
import utilidades
import datetime
import sqlite3
import gestion_reservas as gr

def pedir_fecha():
	## Pedir fecha
	# Pedir año
	ok = 0
	while not ok:
		try:
			ano = int(input("\tInserta año (AAAA): "))
			if ano < datetime.datetime.today().year or ano > datetime.MAXYEAR:
				raise RuntimeError
			ok = 1
		except:
			print("\tEl año introducido no es válido")

	# Pedir mes
	ok = 0
	while not ok:
		try:
			mes = int(input("\tInserta mes (MM = 1-12): "))
			if not int(mes) in range(1, 13):
				raise RuntimeError
			ok = 1
		except:
			print("\tEl mes debe ser un número entre uno y doce.")

	# Pedir día
	ok = 0
	while not ok:
		try:
			dia = int(input("\tInserta día (1-31): "))
			fecha = datetime.datetime(ano, mes, int(dia))
			ok = 1
		except:
			print("\tEl día introducido no es válido.")

	return fecha

def pedir_fecha_hora():
	aux = pedir_fecha()
	h = int(input("Introduce la hora (00-23): "))
	m = int(input("Introduce los minutos (00 o 30): "))
	fecha = datetime.datetime(aux.year, aux.month, aux.day, h, m)
	return fecha


def imprimir_opciones():
	print("\n\n\t****************************")
	print("\t0. Salir")
	print("\t1. Consultar horario")
	print("\t2. Hacer reserva")
	print("\t3. Cancelar reserva")
	print("\t4. Consultar reserva")
	print("\t****************************\n\n")

def consultar_horario_usr():
	fecha = pedir_fecha()
	id = utilidades.obtener_cod_fecha(fecha)
	print(gr.consultar_horario('futbolin',fecha))
	print("\n\n\n")
	utilidades.pausa_ejecucion()

def hacer_reserva_usr():
	print("Hacer reserva")
	fecha = pedir_fecha_hora()

def cancelar_reserva_usr():
	print("hi")

def consultar_reserva_usr():
	print("hi")

def main():
	ok = 0
	res = -1
	nOpciones = 5
	plat = utilidades.plataforma()

	while res:
		ok = 0
		res = -1
		dia = ano = mes = 0

		while not ok:
			if plat is 'Windows':
				utilidades.limpiar_pantalla()

			imprimir_opciones()
			try:
				res = int(input("\tQue quieres hacer? "))
				if not res in range(0, nOpciones):
					raise RuntimeError
				ok = 1
			except:
				print("\tEl valor introducido no es válido.")

		if plat is not 'Windows':
			utilidades.limpiar_pantalla()
		if res == 1:	consultar_horario_usr()
		elif res == 2:	hacer_reserva_usr()
		elif res == 3:	cancelar_reserva_usr()
		elif res == 4:	consultar_reserva_usr()



if __name__ == '__main__':
	main()
