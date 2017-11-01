import os, shelve
import sqlite3 as sq3
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
PORT = 8000
DEBUG = True


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		conn = sq3.connect('datos.db')
		db = conn.cursor()

		session['msg'] = ""

		try:
			usr = str(request.form['usr'])
			pwd = str(request.form['pwd'])
		except:
			session['msg'] = "Los datos introducidos no son válidos"
			usr = 'error'
			pwd = 'error'

		if 'entrar' in request.form:
			query = "SELECT user FROM usuarios WHERE user = '" + usr + "' and pass = '" + pwd + "'"
			db.execute(query)

			if db.fetchone():
				session['logged_in'] = True
				session['usr'] = usr
			else:
				session['msg'] = "Los datos introducidos no se corresponden con los de ningún usuario registrado"

		elif 'registrar' in request.form:
			query = "SELECT user FROM usuarios WHERE user = '" + usr + "'"
			db.execute(query)
			print(query)

			if not db.fetchone():
				query = "INSERT INTO usuarios ('user','pass') VALUES ('" + usr + "','" + pwd + "')"
				print(query)
				session['msg'] = "¡Usuario creado con éxito! Ya puedes acceder..."
			else:
				session['msg'] = "Ya existe un usuario con ese nombre"
		conn.close()
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
