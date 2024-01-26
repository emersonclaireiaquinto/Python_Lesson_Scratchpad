from flask import Flask, render_template, request

app = Flask(__name__) # create a new flask app, __name__ is the name of the current python module

@app.route('/', methods=['GET', 'POST']) # add the methods parameter to the route decorator
def index():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name)
    return render_template('index.html')

app.run() # run the app