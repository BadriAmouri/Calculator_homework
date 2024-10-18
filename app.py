from flask import Flask, jsonify
from Addition import Addition
from Substraction import Substraction
from Multiplication import Multiplication
from Division import Division

app = Flask(__name__)

def handle_invalid_input(error_message):
    return jsonify({'status': 400, 'error': error_message})

@app.route('/add/<inputA>/<inputB>', methods=['GET'])
def add(inputA, inputB):
    try:
        numA = float(inputA)
        numB = float(inputB)

        operation = Addition()
        result = operation.compute(numA, numB)
        return jsonify({'status': 200, 'result': result})

    except ValueError:
        return handle_invalid_input("Invalid input: please provide numeric values.")

@app.route('/minus/<inputA>/<inputB>', methods=['GET'])
def subtract(inputA, inputB):
    try:
        numA = float(inputA)
        numB = float(inputB)

        operation = Substraction()
        result = operation.compute(numA, numB)
        return jsonify({'status': 200, 'result': result})

    except ValueError:
        return handle_invalid_input("Invalid input: please provide numeric values.")

@app.route('/multiply/<inputA>/<inputB>', methods=['GET'])
def multiply(inputA, inputB):
    try:
        numA = float(inputA)
        numB = float(inputB)

        operation = Multiplication()
        result = operation.compute(numA, numB)
        return jsonify({'status': 200, 'result': result})

    except ValueError:
        return handle_invalid_input("Invalid input: please provide numeric values.")

@app.route('/divide/<inputA>/<inputB>', methods=['GET'])
def divide(inputA, inputB):
    try:
        numA = float(inputA)
        numB = float(inputB)

        operation = Division()
        result = operation.compute(numA, numB)
        return jsonify({'status': 200, 'result': result})

    except ValueError:
        return handle_invalid_input("Invalid input: please provide numeric values.")
    except ZeroDivisionError as e:
        return jsonify({'status': 400, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
