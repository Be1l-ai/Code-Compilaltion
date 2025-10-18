import sys
import os

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from flask import Flask, render_template, request
from code_com.calculator.calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
@app.route('/advance_calculator', methods=['GET', 'POST'])
def home():
    result = None
    expression = ""
    
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        if expression:
            result = calc.evaluate_expression(expression)
    elif request.method == 'GET':
        expression = request.args.get('expression', '')
        if expression:
            result = calc.evaluate_expression(expression)
    
    return render_template('advance_calculator.html', result=result, expression=expression)

if __name__ == "__main__":
    print("Starting Flask calculator app...")
    print("Go to: http://127.0.0.1:5000/advance_calculator")
    app.run(debug=True, host='0.0.0.0', port=5000)
