
def consultar_horario(tabla, fecha):
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
