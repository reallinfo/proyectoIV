import platform
import os

def limpiar_pantalla():
	sistema = platform.system()
	if sistema == 'Windows':
		basura = os.system('cls')
	elif sistema == 'Linux' or sistema == 'Darwin':
		basura = os.system('clear')
