import os, pymongo
import sqlite3 as sq3
from urllib import parse
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = os.urandom(12)

PORT = 8000
DEBUG = True

''' Cuando acabe con las pruebas cambiaré la contraseña y quitaré esto. '''
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://prueba:123456@ds245805.mlab.com:45805/base')

print(MONGO_URL)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		client = pymongo.MongoClient(MONGO_URL)
		col = client.base.users_iv
		session['msg'] = ""

		res = col.find()
		try:
			usr = str(request.form['usr'])
			pwd = str(request.form['pwd'])
			res = col.find()
		except:
			session['msg'] = "Los datos introducidos no son válidos"
			usr = 'error'
			pwd = 'error'

		if ('entrar' in request.form) and (usr != 'error'):

			for i in res:
				aux = i
				if (aux['user'] == usr) and (aux['pass'] == pwd):
					session['logged_in'] = True
					session['usr'] = usr

			if not session.get('logged_in'):
				session['msg'] = "Los datos introducidos no se corresponden con los de ningún usuario registrado"

		elif ('registrar' in request.form) and (usr != 'error'):
			existe = False
			for i in res:
				aux = i
				if aux['user'] == usr:
					existe = True

			if existe:
				session['msg'] = "Ya existe un usuario con ese nombre"
			else:
				col.insert_one( {'user':usr, 'pass':pwd} )
				session['msg'] = "¡Usuario creado con éxito! Ya puedes acceder..."
		client.close()
	return render_template('index.html')


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.pop('msg', None)
	session.pop('usr', None)
	return redirect('/')


@app.route('/cambiopass', methods = ['POST'])
def cambiopass():
	client = pymongo.MongoClient(MONGO_URL)
	col = client.base.users_iv
	session['msg'] = "Vamos allá"

	try:
		usr = session.get('usr')
		pwd = str(request.form['anterior'])
		pwdn1 = str(request.form['nueva1'])
		pwdn2 = str(request.form['nueva2'])
	except:
		session['msg'] = "Los datos introducidos no son válidos"
		usr = 'error'
		pwd = 'error'
		pwdn1 = 'error'
		pwdn2 = 'error'

	if pwdn1 != pwdn2:
		session['msg'] = "Las contraseñas introducidas no coinciden"
		usr = 'error'
	elif pwd == pwdn1:
		session['msg'] = "La contraseña nueva debe ser diferente de la actual"
		usr = 'error'

	if not (usr == 'error' or pwd == 'error' or pwdn1 == 'error' or pwdn2 == 'error'):
		res = col.find()
		for i in res:
			aux = i
			if (aux['user'] == usr) and (aux['pass'] == pwd):
				col.update_one( {'user':usr}, {'$set': {'pass':pwdn1} } )
				session['msg'] = "La contraseña se ha actualizado con éxito"
			elif (aux['user'] == usr):
				session['msg'] = "La contraseña introducida como actual no es correcta"

	return redirect('/')



if __name__ == '__main__':
	app.run(port = PORT, debug = DEBUG)
