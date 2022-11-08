from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

dados = ['joao', 33, '525.357.806-97', 'salvador']
@app.route('/')
def index():
    return render_template('pagina4.html', dados_var = dados)

if __name__ == '__main__':
    app.run(debug=True)