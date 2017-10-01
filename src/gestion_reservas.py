import fechas
import utilidades
import datetime
import sqlite3
import gestion_bd

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

def imprimir_opciones():
	print("\n\n\t****************************")
	print("\t0. Salir")
	print("\t1. Consultar horario")
	print("\t2. Hacer reserva")
	print("\t3. Cancelar reserva")
	print("\t4. Consultar reserva")
	print("\t****************************\n\n")

def consultar_horario():
	fecha = pedir_fecha
	con = sqlite3.connect('datos.db')
	c = conn.cursor()
	id = utilidades.obtener_id(fecha)
	res = c.execute("SELECT * FROM futbolin WHERE id = ?", id)

	con.commit()
	con.close()

def hacer_reserva():
	print("hi")

def cancelar_reserva():
	print("hi")

def consultar_reserva():
	print("hi")

def main():

	ok = 0
	res = -1
	nOpciones = 5

	while res:
		ok = 0
		res = -1
		dia = ano = mes = 0

		while not ok:
			utilidades.limpiar_pantalla()
			imprimir_opciones()
			try:
				res = int(input("\tQue quieres hacer? "))
				if not res in range(0, nOpciones):
					raise RuntimeError
				ok = 1
			except:
				print("\tEl valor introducido no es válido.")

		if res == 1:	consultar_horario()
		elif res == 2:	hacer_reserva()
		elif res == 3:	cancelar_reserva()
		elif res == 4:	consultar_reserva()



if __name__ == '__main__':
	main()