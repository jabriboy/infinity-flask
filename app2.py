from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

@app.route('/')
def index():
    var = 'Flask'
    return render_template('pagina2.html', variavel=var)

if __name__ == '__main__':
    app.run(debug=True)