from flask import Flask, request, render_template

app = Flask(__name__)
PORT = 8000
DEBUG = True


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(port = PORT, debug = DEBUG)
