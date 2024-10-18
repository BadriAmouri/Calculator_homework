from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def compute(self, op1, op2):
        pass