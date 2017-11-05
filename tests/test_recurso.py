
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

class TestRecurso(unittest.TestCase):
	def test_creacion(self):
		r = Recurso('prueba', 5, 10)
		print("Testeando constructor... ", end = '')

		self.assertTrue(r.get_t_min() <= r.get_t_max(), "t_min > t_max")
		self.assertTrue(r.get_t_min() > -1, "t_min es menor que cero")
		self.assertTrue(r.get_t_max() > -1, "t_max es menor que cero")
		self.assertTrue(type(r.get_nombre()) == str, "Nombre no es un string")
		print("OK")

	def test_setters(self):
		print("Testeando setters... ", end = '')
		r = Recurso('prueba', 5, 10)
		self.assertFalse(r.set_t_min(-1), "set_t_min acepta números negativos")
		self.assertFalse(r.set_t_min("str"), "set_t_min acepta tipos != int")
		self.assertFalse(r.set_t_max(-1), "set_t_max acepta números negativos")
		self.assertFalse(r.set_t_max("str"), "set_t_max tipos != int")

		r.set_t_max = 3
		self.assertFalse(r.get_t_min() > r.get_t_max(), "set_t_max permite que t_min > t_max")

		r.set_t_min = 13
		self.assertFalse(r.get_t_min() > r.get_t_max(), "set_t_min permite que t_min > t_max")
		print("OK")

if __name__ == '__main__':
	print("INICIANDO TEST DE LA CLASE RECURSO (src/recurso.py)")
	unittest.main()
