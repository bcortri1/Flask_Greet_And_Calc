# Put your app in here.
from flask import Flask, request
import operations as op
app = Flask(__name__)

@app.route("/math/<path>")
def catch_all(path=None):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(eval(f"op.{path}({a},{b})"))

@app.route("/add")
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(op.add(a,b))

@app.route("/sub")
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(op.sub(a,b))

@app.route("/mult")
def mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(op.mult(a,b))

@app.route("/div")
def div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(op.div(a,b))
