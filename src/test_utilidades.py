import unittest
from fechas import *
from utilidades import *

class TestUtilidades(unittest.TestCase):
	def test_obtener_id(self):
		print("Testeando obtener_id()...")
		fecha = datetime.datetime(2020, 12, 1, 1, 2)
		res = obtener_id(fecha)
		self.assertEqual(type(res), str, "Devuelve un tipo de dato incorrecto")
		self.assertEqual(len(res), 13, "Devuelve una cadena de tamaño diferente al que debería")
		self.assertEqual(res[8], ":", "No tiene ':' que separen fecha y hora")
		self.assertEqual(obtener_fecha(res), fecha, "El código obtenido no coincide con la fecha dada")

	def test_obtener_fecha(self):
		print("Testeando obtener_fecha()... ")
		fecha = datetime.datetime(2020, 12, 1, 1, 2)
		id = obtener_id(fecha)
		res = obtener_fecha(id)
		self.assertEqual(type(res), datetime.datetime, "Devuelve un tipo de dato incorrecto")
		self.assertEqual(obtener_id(res), id, "El código obtenido no coincide con la fecha dada")

	def test_obtener_cod_fecha(self):
		print("Testeando obtener_cod_fecha")
		fecha = datetime.datetime(2020, 12, 1)
		res = obtener_cod_fecha(fecha)
		self.assertEqual(len(res), 8, "La longitud del string no es la correcta")
		self.assertEqual(type(res), str, "El tipo devuelto no es correcto")

	def test_obtener_cod_hora(self):
		print("Testeando obtener_fecha()... ")
		fecha = datetime.datetime(2020, 12, 1, 1, 2)
		res = obtener_cod_hora(fecha)
		self.assertEqual(len(res), 4, "La longitud del string no es la correcta")
		self.assertEqual(type(res), str, "El tipo devuelto no es correcto")


if __name__ == '__main__':
	print("INICIANDO TEST DE LA BIBILIOTECA DE UTILIDADES (utilidades.py)")
	unittest.main()
