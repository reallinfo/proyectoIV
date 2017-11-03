import os, shelve, pymongo
import sqlite3 as sq3
from urllib import parse
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
PORT = 8000
DEBUG = True




@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		session['msg'] = ""

		try:
			usr = str(request.form['usr'])
			pwd = str(request.form['pwd'])
		except:
			session['msg'] = "Los datos introducidos no son válidos"
			usr = 'error'
			pwd = 'error'

		if ('entrar' in request.form) and (usr != 'error'):
			session['logged_in'] = True
			session['usr'] = usr

			if not session['logged_in']:
				session['msg'] = "Los datos introducidos no se corresponden con los de ningún usuario registrado"
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
