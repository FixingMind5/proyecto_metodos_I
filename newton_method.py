"""Newton Method Module"""
from numeric_method import NumericMethod
from math import sin

class NewtonMethod(NumericMethod):
    """Newton method to find the roots of a function"""
    value = float

    def __init__(self, value, tolerance, decimal_to_round):
        """overrides super constructor.

        @param value: the value of axis x
        """
        super().__init__(
            x_0=None,
            x=None,
            tolerance=tolerance,
            decimal_to_round=decimal_to_round
        )
        self.value = value

    def function_prime(self, value):
        """Holds the first derivative of the
        given function
        
        @param value: the given value
        @returns the value evaluated
        """

        return (-1 * sin(value)) - 1
    
    def newton_method_function(self, value):
        """Implements the function that'll be used in
        newton method
        
        @param value: the value that'll be evaluated
        @returns the evaluation of this value (Xn+1)
        """
        result = 0.0
        result = self.function(value)
        result /= self.function_prime(value)
        
        return value - result
    
    def solve(self):
        """finds the root with the given value"""
        value =  self.value
        iteration = 0
        converge = False
        max_iterations = int
        max_iterations_message = (
            "Ingresa el número de iteraciones a realizar, "
            "debe de ser un número entero: "
        )

        while True:
            try:
                max_iterations = int(input(max_iterations_message))
                break
            except TypeError:
                print("Tiene que ser un número entero")
                continue

        while iteration <= max_iterations:
            if iteration == 0:
                f_x = self.function(value)
                if f_x == 0:
                    converge = True
                    print(f"Una raíz de la ecuacion es {value}")
                    break
            
            next_x = self.newton_method_function(value)
            f_next_x = self.function(next_x)

            if f_next_x == 0:
                converge = True
                print(f"Una raiz de la ecuación dada es {next_x}")
                break
            
            if iteration > 0:
                error = self.absolute_error(value, next_x)
                if error <= self.TOLERANCE and abs(f_x) <= self.TOLERANCE:
                    print(f"Una raiz aproximada de la ecuación dada es {value}")
                    converge = True
                    break
            
            value = next_x
            iteration += 1
        
        if not converge:
            print("El método no converge a una raiz")
