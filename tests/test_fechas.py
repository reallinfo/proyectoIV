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
		with self.assertWarns(UserWarning):
			ayer('string')

	def test_hoy(self):
		print("Testeando hoy()...")
		self.assertEqual(type(hoy()).__name__, 'datetime', "hoy() no ha devuelto un tipo datetime")
		self.assertEqual(type(hoy(5)).__name__, 'datetime', "hoy() no ha devuelto un tipo datetime")
		with self.assertWarns(UserWarning):
			hoy('string')

	def test_manana(self):
		print("Testeando manana()...")
		self.assertEqual(type(manana()).__name__, 'datetime', "manana() no ha devuelto un tipo datetime")
		self.assertEqual(type(manana(5)).__name__, 'datetime', "manana() no ha devuelto un tipo datetime")
		self.assertEqual(fecha_pasada(manana()), False)
		with self.assertWarns(UserWarning):
			manana('string')

	def test_fecha_pasada(self):
		print("Testeando fecha_pasada()...")
		self.assertTrue(fecha_pasada(ayer()), "Ayer no ha sido determinada como fecha pasada")
		self.assertTrue(fecha_pasada(hoy()), "Hoy no ha sido determinado como fecha pasada")
		self.assertFalse(fecha_pasada(manana()), "Mañana ha sido determinado como fecha pasada")
		# self.assertRaises(Exception, fecha_pasada(9), "fecha_pasada() no da error cuando le pasas un string")
		with self.assertRaises(TypeError):
			fecha_pasada(9)

	def test_fecha_entre(self):
		print("Testeando fecha_entre()...")
		x = datetime.now()
		self.assertTrue(fecha_entre(hoy(), ayer(), manana()), "Se ha determinado que hoy no está entre ayer y manañana")
		self.assertFalse(fecha_entre(ayer(), hoy(), manana()), "Se ha determinado que ayer está entre hoy y mañana")
		with self.assertRaises(TypeError):
			fecha_entre(9, x, x)
		with self.assertRaises(TypeError):
			fecha_entre(x, 9, x)
		with self.assertRaises(TypeError):
			fecha_entre(x, x, 9)

	def test_hora_pasada(self):
		print("Testeando hora_pasada()...")
		self.assertTrue(hora_pasada(datetime.now()))
		x = datetime(datetime.now().year+1, 12, 12)
		self.assertFalse(hora_pasada(x))
		with self.assertRaises(TypeError):
			hora_pasada(5)

if __name__ == '__main__':
	print("INICIANDO TEST DE LA BIBILIOTECA DE FECHAS (src/fechas.py)")
	unittest.main()
