"""Secant method module"""
from math import cos
import numpy as np
import matplotlib.pyplot as plt

class NumericMethod:
    """Numeric method class"""
    x_0 = float
    x = float
    function_name = ""
    TOLERANCE = float
    ROUND = None

    def __init__(self, x_0, x, tolerance, decimal_to_round=None):
        """Constructor of method

        @param x_0: the first value of interval or
        the first value that'll be used
        @param x: the second value of interval or
        the second value
        """
        self.x_0 = x_0
        self.x = x
        self.TOLERANCE = 1 * pow(10, tolerance)
        if decimal_to_round:
            self.ROUND = decimal_to_round

    def function(self, value):
        """holds the function will be evaluated
        
        @param value: float or int, the value that'll be
        evaluated
        @returns value evaluated
        """
        self.function_name = "cos(x) - x"
        return cos(value) - value

    def absolute_error(self, first_value, second_value):
        """Obtain the absolute value of two numbers given
        
        @param first_value: the first number to be used
        @param second_value: the second number to be used

        @returns the absolute error
        """
        result = 0.0
        result = second_value - first_value
        result /= second_value

        return abs(result)
    
    def tabulate(self, interval=None, step=1):
        """Gets the values of the tabulation of a function

        @param interval: A list with [start, end]
        @param steps: how much will grow up the function
        @returns a list with the results of tabulation
        """
        (start, end) = (interval[0], interval[1])
        axis_x_list = np.arange(start, end + 1, step)
        result_list = [
            round(self.function(element), self.ROUND) 
            if self.ROUND 
            else self.function(element)
            for element 
            in axis_x_list
        ]

        print("\nx \t | \t y")
        for index in range(len(axis_x_list)):
            x_value = round(axis_x_list[index], self.ROUND) if self.ROUND else axis_x_list[index]
            print(f"{x_value} \t | \t {result_list[index]}")

        return (axis_x_list, result_list)
    
    def plot(self, axis_x, axis_y):
        """Plots a function with given values
        
        @param axis_y: a list of values of x axis
        @param axis_y: a list of values of y axis
        """
        plt.plot(axis_x, axis_y)
        plt.title(f"grafica de la función {self.function_name}")
        plt.xlabel("eje x")
        plt.ylabel("eje y")
        plt.show()

    def solve(self):
        """prototype function

        override it in order to make it work"""
        pass
