from flask import (
    Flask,
    redirect,
    url_for
)

app = Flask(__name__)

@app.route('/')
def home():
    return 'admin or guest?'

@app.route('/admin/<admin>')
def hello_admin(admin):
    return f'ola admin {admin}'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'ola guest {guest}'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'Maria':
        return redirect(url_for('hello_admin', admin = name))
    
    return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__':
    app.run(debug=True)