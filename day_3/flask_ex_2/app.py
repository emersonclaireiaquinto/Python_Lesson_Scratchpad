from flask import Flask, render_template

app = Flask(__name__) # create a new flask app, __name__ is the name of the current python module

@app.route('/')
def index():
    return render_template('index.html')

app.run() # run the app