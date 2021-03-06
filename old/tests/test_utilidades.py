"""
Tests del archivo src/utilidades.py
"""


# Modificación del path para incluir las demás carpetas, por comodidad a la hora de importar.
import sys, platform
if platform.system is 'Windows':
	sys.path.append(".\src")
else:
	sys.path.append("./src")

import unittest
from fechas import *
from utilidades import *

class TestUtilidades(unittest.TestCase):
	def test_otros(self):
		print("Testeando utilidades varias...")
		limpiar_pantalla()
		pausa_ejecucion()
		self.assertTrue(type(plataforma()) is str)
		self.assertTrue(len(obtener_ano("20201111")) == 4)
		self.assertTrue(len(obtener_mes("20201111")) == 2)
		self.assertTrue(len(obtener_dia("20201111")) == 2)

	def test_obtener_id(self):
		print("Testeando obtener_id()...")
		fecha = datetime.datetime(2020, 12, 1, 1, 2)
		res = obtener_id(fecha)
		self.assertEqual(type(res), str, "Devuelve un tipo de dato incorrecto")
		self.assertEqual(len(res), 13, "Devuelve una cadena de tamaño diferente al que debería")
		self.assertEqual(res[8], ":", "No tiene ':' que separen fecha y hora")
		self.assertEqual(obtener_fecha(res), fecha, "El código obtenido no coincide con la fecha dada")

		with self.assertRaises(TypeError):
			obtener_id(5)


	def test_obtener_fecha(self):
		print("Testeando obtener_fecha()... ")
		fecha = datetime.datetime(2020, 12, 1, 1, 2)
		id = obtener_id(fecha)
		res = obtener_fecha(id)
		self.assertEqual(type(res), datetime.datetime, "Devuelve un tipo de dato incorrecto")
		self.assertEqual(obtener_id(res), id, "El código obtenido no coincide con la fecha dada")
		with self.assertRaises(TypeError):
			obtener_fecha(6)

	def test_obtener_cod_fecha(self):
		print("Testeando obtener_cod_fecha")
		fecha = datetime.datetime(2020, 12, 1)
		fecha2 = datetime.datetime(2020, 1, 11)
		res = obtener_cod_fecha(fecha)
		res2 = obtener_cod_fecha(fecha2)
		self.assertEqual(len(res), 8, "La longitud del string no es la correcta")
		self.assertEqual(type(res), str, "El tipo devuelto no es correcto")
		self.assertEqual(len(res2), 8, "La longitud del string no es la correcta")
		self.assertEqual(type(res2), str, "El tipo devuelto no es correcto")

		with self.assertRaises(TypeError):
			obtener_cod_fecha(5)

	def test_obtener_cod_hora(self):
		print("Testeando obtener_fecha()... ")
		fecha = datetime.datetime(2020, 12, 1, 1, 2)
		fecha2 = datetime.datetime(2020, 12, 1, 11, 22)
		res = obtener_cod_hora(fecha)
		res2 = obtener_cod_hora(fecha2)
		self.assertEqual(len(res), 4, "La longitud del string no es la correcta")
		self.assertEqual(type(res), str, "El tipo devuelto no es correcto")

		with self.assertRaises(TypeError):
			obtener_cod_hora(5)

if __name__ == '__main__':
	print("INICIANDO TEST DE LA BIBILIOTECA DE UTILIDADES (src/utilidades.py)")
	unittest.main()
