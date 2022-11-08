from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pagina5-get.html')

@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():
    if request.method == 'GET':
        usuario = request.args.get('usuario')
        senha = request.args.get('senha')

    return f'usuario: {usuario}, senha: {senha}'


if __name__ == '__main__':
    app.run(debug=True)