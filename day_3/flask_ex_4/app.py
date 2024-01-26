from flask import Flask, render_template, request, make_response

app = Flask(__name__) # create a new flask app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        response = make_response(render_template('index.html', name=name))
        response.set_cookie('name', name)
        return response
    return render_template('index.html')

app.run() # run the app