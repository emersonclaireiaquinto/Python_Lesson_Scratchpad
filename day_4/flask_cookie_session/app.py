from flask import Flask, render_template, request, make_response, redirect, url_for, session

app = Flask(__name__) # create a new flask app

app.secret_key = 'BAD_SECRET_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    args = request.args
    key = args.get('key')
    value = args.get('value')
    return render_template('index.html', key=key, value=value)

@app.route('/getcookie', methods=['POST'])
def getcookie():
    key = request.form['key']
    value = request.cookies.get(key)
    return redirect(url_for('index', key=key, value=value))

@app.route('/setcookie', methods=['POST'])
def setcookie():
    key = request.form['key']
    value = request.form['value']
    max_age = int(request.form['max_age'])
    response = make_response(redirect(url_for('index')))
    response.set_cookie(key, value, max_age=max_age)
    return response

@app.route('/deletecookie', methods=['POST'])
def deletecookie():
    key = request.form['key']
    response = make_response(redirect(url_for('index')))
    response.delete_cookie(key)
    return response

@app.route('/clearcookies', methods=['POST'])
def clearcookies():
    response = make_response(redirect(url_for('index')))
    for key in request.cookies:
        response.delete_cookie(key)
    return response
    
@app.route('/setsession', methods=['POST'])
def setsession():
    key = request.form['key']
    value = request.form['value']
    session[key] = value
    return redirect(url_for('index'))

@app.route('/getsession', methods=['POST'])
def getsession():
    key = request.form['key']
    value = session.get(key)
    return redirect(url_for('index', key=key, value=value))

@app.route('/deletesession', methods=['POST'])
def deletesession():
    key = request.form['key']
    session.pop(key, None)
    return redirect(url_for('index'))

@app.route('/clearsessions', methods=['POST'])
def clearsessions():
    session.clear()
    return redirect(url_for('index'))


app.run() # run the app