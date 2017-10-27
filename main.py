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


if __name__ == '__main__':
	app.run(port = PORT, debug = DEBUG)
