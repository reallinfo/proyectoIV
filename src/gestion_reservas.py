import fechas
import utilidades
import datetime

def pedir_fecha():
	## Pedir fecha
	# Pedir año
	ok = 0
	while not ok:
		try:
			ano = int(input("\tInserta año (AAAA): "))
			if ano < datetime.datetime.today().year:
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

		if res:
			fecha = pedir_fecha()



if __name__ == '__main__':
	main()
