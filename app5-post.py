from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pagina5-post.html')

@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

    return f'usuario: {usuario}, senha: {senha}'


if __name__ == '__main__':
    app.run(debug=True)