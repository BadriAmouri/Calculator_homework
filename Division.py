from Calculator import Calculator

class Division(Calculator):
    def compute(self, op1, op2):
        if op2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return op1 / op2
