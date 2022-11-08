from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

nome = 'Maria'
dados = {
    'idade': 23,
    'profissao': 'médica',
    'RG': '12234556',
    'cidade': 'salvador'
}

@app.route('/')
def index():
    return render_template('pagina3.html', nome_var = nome, dados_var = dados)

if __name__ == '__main__':
    app.run(debug=True)