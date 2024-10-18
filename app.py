from flask import Flask, jsonify
from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division

app = Flask(__name__)

def handle_operation(operation, numA, numB):
    try:
        result = operation.compute(numA, numB)
        return jsonify({'status': 200, 'result': result})
    except ZeroDivisionError as e:
        return jsonify({'status': 400, 'error': str(e)})
    except Exception as e:  # Catch any other unexpected errors
        return jsonify({'status': 500, 'error': 'An unexpected error occurred: ' + str(e)})

@app.route('/add/<int:numA>/<int:numB>', methods=['GET'])
def add(numA, numB):
    operation = Addition()
    return handle_operation(operation, numA, numB)

@app.route('/minus/<int:numA>/<int:numB>', methods=['GET'])
def subtract(numA, numB):
    operation = Subtraction()
    return handle_operation(operation, numA, numB)

@app.route('/multiply/<int:numA>/<int:numB>', methods=['GET'])
def multiply(numA, numB):
    operation = Multiplication()
    return handle_operation(operation, numA, numB)

@app.route('/divide/<int:numA>/<int:numB>', methods=['GET'])
def divide(numA, numB):
    operation = Division()
    return handle_operation(operation, numA, numB)

if __name__ == '__main__':
    app.run(debug=True)
