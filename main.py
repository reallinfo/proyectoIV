import os
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
PORT = 8000
DEBUG = True


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.form['pwd'] == 'pass' and request.form['usr'] == 'user':
			session['logged_in'] = True
		print("POST")
	else:
		print("GET")

	if 'entrar' in request.form:
		print("Entrar")
	elif 'registrar' in request.form:
		print("Registrar")
	'''print(request.form['registrar'])'''

	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		return render_template('index.html')

@app.route('/logout')
def logout():
	session.pop('logged_in')
	return redirect('/')


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(port = PORT, debug = DEBUG)
