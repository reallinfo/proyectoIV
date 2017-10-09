"""
Tests del archivo src/fechas.py
"""


# Modificación del path para incluir las demás carpetas, por comodidad a la hora de importar.
import sys, platform
if platform.system is 'Windows':
	sys.path.append(".\src")
else:
	sys.path.append("./src")

import unittest
from fechas import *
from datetime import *


class TestFechas(unittest.TestCase):
	def test_ayer(self):
		print("Testeando ayer()...")
		self.assertEqual(type(ayer()).__name__, 'datetime', "ayer() no ha devuelto un tipo datetime")
		self.assertEqual(type(ayer(5)).__name__, 'datetime', "ayer() no ha devuelto un tipo datetime")
		self.assertEqual(fecha_pasada(ayer()), True)

	def test_hoy(self):
		print("Testeando hoy()...")
		self.assertEqual(type(hoy()).__name__, 'datetime', "hoy() no ha devuelto un tipo datetime")
		self.assertEqual(type(hoy(5)).__name__, 'datetime', "hoy() no ha devuelto un tipo datetime")

	def test_manana(self):
		print("Testeando manana()...")
		self.assertEqual(type(manana()).__name__, 'datetime', "manana() no ha devuelto un tipo datetime")
		self.assertEqual(type(manana(5)).__name__, 'datetime', "manana() no ha devuelto un tipo datetime")
		self.assertEqual(fecha_pasada(manana()), False)

	def test_fecha_pasada(self):
		print("Testeando fecha_pasada()...")
		self.assertTrue(fecha_pasada(ayer()), "Ayer no ha sido determinada como fecha pasada")
		self.assertTrue(fecha_pasada(hoy()), "Hoy no ha sido determinado como fecha pasada")
		self.assertFalse(fecha_pasada(manana()), "Mañana ha sido determinado como fecha pasada")

	def test_fecha_entre(self):
		print("Testeando fecha_entre()...")
		self.assertTrue(fecha_entre(hoy(), ayer(), manana()), "Se ha determinado que hoy no está entre ayer y manañana")


if __name__ == '__main__':
	print("INICIANDO TEST DE LA BIBILIOTECA DE FECHAS (src/fechas.py)")
	unittest.main()
