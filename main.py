from flask import Flask, request, render_template

app = Flask(__name__)
PORT = 8000
DEBUG = True


@app.route('/', methods=['GET', 'POST'])
def index():
	nombre = ""
	if request.method == 'POST':
		nombre = request.form.get('id')
		nombre = str(nombre)
		print(str(nombre))

	return render_template('index.html', nombre = nombre)

@app.route('/pag1')
def pag1():
	return render_template('pag1.html')

@app.route('/pag2')
def pag2():
	return render_template('pag2.html')

@app.route('/cal', methods=['GET', 'POST'])
def calc():
	variables = [0, 0, 0, False]
	if request.method == 'POST':
		n1 = request.form.get('n1')
		n2 = request.form.get('n2')
		try:
			res = int(n1) + int(n2)
			ok = True
		except:
			res = -1
			ok = False
		variables = [n1, n2, res, ok]

	print(variables)

	return render_template('cal.html', variables = variables)

if __name__ == '__main__':
	app.run(port = PORT, debug = DEBUG)
