#-*- coding: utf-8 -*-
__author__ = 'coolfire'
from flask import Flask,abort,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for("/login"))


@app.route('/login')
def login():
    abort(401)
    this_is_nerver_executed()

if __name__ == "__main__":
    app.run()