from flask import Flask

app = Flask(__name__) # create a new flask app, __name__ is the name of the current python module

@app.route('/') # this is a decorator, it tells flask what URL should trigger the function below
def hello_world(): 
    return 'Hello, Worldsdfsef!' 


@app.route('/home')
def home():
    return '<h1>The home page</h1>'

app.run() # run the app