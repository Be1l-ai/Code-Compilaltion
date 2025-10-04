from flask import Flask, render_template, request
from ..calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/advance_calculator', methods=['GET'])
def home():
    if request.method == 'GET':
        input = request.args.get('result')
        result = calc.evaluate_expression(input)
        if result:
            return render_template('advance_calculator.html', result=result)
    return render_template('advance_calculator.html')

if __name__ == "__main__":
    app.run(debug=True)
