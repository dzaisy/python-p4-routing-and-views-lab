#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h2>string: {parameter}</h2>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(1, parameter + 1))
    return f'<h2>counted:</h2><pre>{numbers}</pre>'

@app.route('/math/<int:num1>/<operation>/<int:num2>.')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else: 
            return 'you CANNOT divide by 0'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'operation invalid'
    return f'<h2>result of {num1} {operation} {num2} = {result}</h2>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
