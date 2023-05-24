#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:my_string>')
def print_string(my_string):
    print(my_string)
    return f'{my_string}'

@app.route('/count/<int:my_integer>')
def count(my_integer):
    return_string = ""
    for num in range(my_integer):
        return_string += str(num) + "\n"
    return return_string
    
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    operation_dict = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "div": num1 / num2,
        "%": num1 % num2
    }
    if operation in operation_dict:
        return str(operation_dict[operation])
    else:
        return '<h1>That is not a valid operation</h1>'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
