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
		print("Testeando obtener_fecha()...")
		fecha = datetime.datetime(2020, 12, 1, 1, 2)
		id = obtener_id(fecha)
		res = obtener_fecha(id)
		self.assertEqual(type(res), datetime.datetime, "Devuelve un tipo de dato incorrecto")
		self.assertEqual(obtener_id(res), id, "El código obtenido no coincide con la fecha dada")



if __name__ == '__main__':
	print("INICIANDO TEST DE LA BIBILIOTECA DE UTILIDADES (utilidades.py)")
	unittest.main()
