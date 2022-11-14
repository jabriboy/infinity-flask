from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def calculo():
    imc = ''
    if request.method == 'POST':
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        imc = round(peso/((altura/100)**2), 1)

    return render_template("imc.html", imc = imc)

if __name__ == '__main__':
    app.run(debug=True) 