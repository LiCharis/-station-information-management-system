from flask import Flask, send_file, redirect

app = Flask(__name__)



@app.route('/index')
def index():
    return send_file('templates/index.html')


@app.route('/user/login')
def login():
    return send_file('templates/login.html')

@app.route('/user/manager_login')
def manager_login():
    return send_file('templates/manager_login.html')

@app.route('/user/register')
def register():
    return send_file('templates/register.html')


@app.route('/token/index')
def token_index():
    return send_file('templates/token_index.html')



@app.route('/token/manager_index')
def token_manage_index():
    return send_file('templates/token_manage_index.html')

@app.route('/')
def to_index():
    return redirect('/index')

if __name__ == '__main__':
    app.run(debug=True)