'''
Clase que representa a un recurso de la facultad. Un recurso debe tener:
	* Un nombre único que lo diferencia del resto de recursos.
	* Un horario de uso
	* Un calendario de uso
	* Un horario de reservas
	* Un calendario de reservas
	* Un tiempo mínimo durante el que puede ser reservado en minutos
	* Un tiempo máximo que puede reservarse en minutos

Cada recurso tendrá su documento en la colección recursos_iv de la base de datos. Los recursos podrán ser añadidos por usuarios con permisos de administrador, consultados por cualquier usuario y reservados por usuarios que hayan hecho log in.
'''

import warnings

class Recurso:
	def __init__(self, nombre, t_min, t_max):
		try:
			nombre = str(nombre)
			t_min = int(t_min)
			t_max = int(t_max)
			if t_min < 0 or t_max < 0:
				raise ValueError
		except ValueError:
			''' valores por defecto '''
			warnings.warn("Usando valores por defecto", UserWarning)
			nombre = "error"
			t_min = 0
			t_max = 0

		self.nombre = nombre
		if t_min > t_max:
			aux = t_max
			t_max = t_min
			t_min = aux
			print("t_min > t_max, valores cambiados")
		self.t_min = t_min
		self.t_max = t_max


	''' Getters '''
	def get_nombre(self):
		return self.nombre

	def get_t_min(self):
		return self.t_min

	def get_t_max(self):
		return self.t_max


	''' Setters '''
	def set_nombre(self, nombre):
		try:
			nombre = str(nombre)
			self.nombre = nombre
			return True
		except:
			return False


	def set_t_min(self, t_min):
		try:
			t_min = int(t_min)
			if t_min < 0:
				raise ValueError
			if t_min > self.t_max:
				self.t_min = self.t_max
				self.t_max = t_min
			else:
				self.t_min = t_min
			return True
		except:
			return False


	def set_t_max(self, t_max):
		try:
			t_max = int(t_max)
			if t_max < 0:
				raise ValueError
			if t_max < self.t_min:
				self.t_max = self.t_min
				self.t_min = t_max
			else:
				self.t_max = t_max
			return True
		except:
			return False


	def __str__(self):
		return str(self.nombre) + ": " + str(self.t_min) + ", " + str(self.t_max)
