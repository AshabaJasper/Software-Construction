import math
from matplotlib import mathtext


class Calculator:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
    def exponentiate(self, x, y):
        # Raises x to the power of y.
        return x ** y

    def square_root(self, x):
        # # Calculates the square root of x.
        return math.sqrt(x)

    def absolute_value(self, x):
        # # Calculates the absolute value of x.
        return abs(x)