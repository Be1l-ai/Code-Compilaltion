from flask import Flask, render_template, request
from ..calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route('/advance_calculator', methods=['GET'])
def home():
    if request.method == 'GET':
        input = request.args.get('input')
        operation = request.args.get('operation')
        calculation = request.args.get('calculation')
        if calculation:
            result = eval(calculation)
            return render_template('advance_calculator.html', result=result)
    return render_template('advance_calculator.html', input=input, operation=operation)
