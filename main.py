import os, shelve
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
PORT = 8000
DEBUG = True


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		db = shelve.open('usuarios.db')
		session['msg'] = ""

		try:
			usr = str(request.form['usr'])
			pwd = str(request.form['pwd'])
		except:
			session['msg'] = "Los datos introducidos no son válidos"
			usr = 'error'
			pwd = 'error'

		if 'entrar' in request.form:
			if (usr in db) and (db[usr] == pwd):
				session['logged_in'] = True
				session['usr'] = usr
			else:
				session['msg'] = "Los datos introducidos no se corresponden con los de ningún usuario registrado"
		elif 'registrar' in request.form:
			if (usr not in db):
				db['usr'] = pwd
				session['msg'] = "¡Usuario creado con éxito! Ya puedes acceder..."
			else:
				session['msg'] = "Ya existe un usuario con ese nombre"

		db.close()

	if not session.get('logged_in'):
		return render_template('index.html')
	else:
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
