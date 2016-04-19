#-*- coding: utf-8 -*-
__author__ = 'coolfire'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return "Hello world"

if __name__ == '__main__':
    app.run()