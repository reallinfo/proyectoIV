"""
Módulo para dar órdenes directas a la base de datos. Cada una de las funciones recibe una serie de parámetros que usará para interactuar con la base de datos y devuelve algo dependiendo del resultado obtenido de ésta. La idea es separar la interfaz de usuario de la gestión de la base de datos de forma que en el programa principal no haya ninguna referencia a ésta, sólo llamadas a esta biblioteca que hará tareas concretas.
"""


import sqlite3
import utilidades


def consultar_horario(tabla, fecha):
	""" Recibe como parámetros un string con el nombre de la tabla a consultar y una fecha (datetime). Devuelve una lista de horas con las horas ocupadas (de momento devuelven un string superchustero) """
	con = sqlite3.connect('datos.db')
	c = con.cursor()
	cod_fecha = utilidades.obtener_cod_fecha(fecha)
	ok = 0

	query = "SELECT * FROM " + str(tabla) + " WHERE fecha = " + cod_fecha + " ORDER BY hora"
	res = c.execute(query)
	ret = "\tRESERVAS PARA EL " + utilidades.obtener_dia(cod_fecha) + "/" + utilidades.obtener_mes(cod_fecha) + "/" + utilidades.obtener_ano(cod_fecha) + "\n\n"

	aux = res.fetchone()
	while aux != None:
		ok = 1
		ret += "\t" + aux[3][0] + aux[3][1] + ":" + aux[3][2] + aux[3][3] + "\n"
		aux = res.fetchone()

	if not ok:
		ret = "No hay reservas para este día"
	else:
		ret += "\nEl resto de horas están libres."

	con.close()
	return ret
