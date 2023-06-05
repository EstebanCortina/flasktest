from markupsafe import escape
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    value = 10
    return render_template('index.html', value=value)

# el 'f' antes de una cadena es el equivalente de interpolar en JS.


@app.route('/name/<name>/<int:age>')
def hello(name, age):
    return f'Flask test: {name} & {age}'

# Con escape lo que hacemos es convertir el parametro a un texto plano, en este caso el tipo path hace que acepte caracteres propios de codigos o rutas pero al momento de pasarlo, si no lo escapamos, esto se puede ejecutar.


@app.route('/escape/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

# POST


@app.route('/form', methods=['GET', 'POST'])
def form():
    print(request.method)
    if (request.method == 'POST'):
        print(request.form['name'])
        print(request.form['pass'])
        return jsonify(message='success'), 200
    return render_template('form.html')
