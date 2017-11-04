import os, shelve, pymongo
import sqlite3 as sq3
from urllib import parse
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
PORT = 8000
DEBUG = True
MONGO_URL = os.environ.get('MONGO_URL', "error db")

print(MONGO_URL)



@app.route('/hiii')
def getvar():
	return str(MONGO_URL)

''' mongodb://prueba:123456@ds245805.mlab.com:45805/basec '''
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		client = pymongo.MongoClient(MONGO_URL)
		col = client.base.users_iv
		session['msg'] = ""

		res = col.fing()
		r = "<br/>"
		for i in res:
			r += i + "<br/>"

		try:
			usr = str(request.form['usr'])
			pwd = str(request.form['pwd'])
			res = col.find()
		except:
			session['msg'] = "Los datos introducidos no son válidos"
			usr = 'error'
			pwd = 'error'

		if ('entrar' in request.form) and (usr != 'error'):
			session['logged_in'] = True
			session['usr'] = usr

			for i in res:
				aux = i
				if (aux['user'] == usr) and (aux['pass'] == pwd):
					session['logged_in'] = True
					session['usr'] = usr

			if not session['logged_in']:
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
	session.pop('logged_in')
	session.pop('msg')
	session.pop('usr')
	return redirect('/')


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(port = PORT, debug = DEBUG)
