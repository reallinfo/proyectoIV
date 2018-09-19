
"""
Tests del archivo src/recurso.py
"""


# Modificación del path para incluir las demás carpetas, por comodidad a la hora de importar.
import sys, platform
if platform.system is 'Windows':
	sys.path.append(".\src")
else:
	sys.path.append("./src")

import unittest
from recurso import Recurso

class FallaStr(object):
	''' Clase auxiliar que hace fallar el método str() para probar algunas funcionalidades. '''
	def __str__(self):
		raise Exception

class TestRecurso(unittest.TestCase):
	def test_creacion(self):
		r = Recurso('prueba', 5, 10)
		r2 = Recurso('prueba', 10, 5)
		print("Testeando constructor... ", end = '')

		self.assertTrue(r.get_t_min() <= r.get_t_max(), "t_min > t_max")
		self.assertTrue(r2.get_t_min() <= r2.get_t_max(), "t_min > t_max")
		self.assertTrue(r.get_t_min() > -1, "t_min es menor que cero")
		self.assertTrue(r.get_t_max() > -1, "t_max es menor que cero")
		self.assertTrue(type(r.get_nombre()) == str, "Nombre no es un string")
		with self.assertWarns(UserWarning):
			r = Recurso('prueba', 'x', 2)
		with self.assertWarns(UserWarning):
			r = Recurso('prueba', -5, 10)
		print("OK")

	def test_setters(self):
		print("Testeando setters... ", end = '')
		r = Recurso('prueba', 5, 20)
		self.assertFalse(r.set_t_min(-1), "set_t_min acepta números negativos")
		self.assertFalse(r.set_t_min("str"), "set_t_min acepta tipos != int")
		self.assertFalse(r.set_t_max(-1), "set_t_max acepta números negativos")
		self.assertFalse(r.set_t_max("str"), "set_t_max tipos != int")
		self.assertTrue(r.set_nombre("str"), "El nombre no se cambia correctamente")
		self.assertFalse(r.set_nombre(FallaStr()), "str() no da error")


		r.set_t_max(21)
		self.assertFalse(r.get_t_min() > r.get_t_max(), "set_t_max permite que t_min > t_max")

		r.set_t_min(20)
		self.assertFalse(r.get_t_min() > r.get_t_max(), "set_t_min permite que t_min > t_max")

		r.set_t_min(22)
		self.assertFalse(r.get_t_min() > r.get_t_max(), "set_t_min permite que t_min > t_max")

		r.set_t_max(1)
		self.assertFalse(r.get_t_min() > r.get_t_max(), "set_t_max permite que t_min > t_max")
		print("OK")

	def test_print(self):
		r = Recurso('algo', 2, 3)
		self.assertTrue(type(str(r)) is str, "La función de impresión no devuelve str")
		

if __name__ == '__main__':
	print("INICIANDO TEST DE LA CLASE RECURSO (src/recurso.py)")
	unittest.main()
