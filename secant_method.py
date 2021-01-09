"""Secant Method module"""
from numeric_method import NumericMethod


class SecantMethod(NumericMethod):
    """Secant method class"""

    def secant_method(self, previous_value, value):
        """The secant method itself

        @param previous_value: first value of interval
        @param previous_value: second value of interval

        @returns the result of the ecaluation
        """
        result = value - previous_value
        result /= self.function(value) - self.function(previous_value)
        result *= self.function(value)

        return value - result

    def solve(self):
        """Solves the problem
        
        @raise ValueError if the number of iterations isn't at
        leasts 2
        """
        iteration = 1
        (previous_n, n, next_n) = (self.x_0, self.x, 0.0)
        (f_previous_x, f_x, f_next_x) = (0.0, 0.0, 0.0)
        error = 0.0
        MAX_ITERATIONS = int(input("Número de iteraciones a realizar: "))

        if MAX_ITERATIONS <= 1:
            raise ValueError("Asegurate de usar al menos 2 iteraciones")

        print("Comienza el metodo")
        print(f"Iteracion | Xi | Xi+1 | f(Xi) | f(Xi+1) | error absoluto")
        print(
            f"{iteration} \t | {n} | {next_n} | {f_previous_x} | {f_x} | {error if error else '' }")

        while iteration <= MAX_ITERATIONS:
            f_previous_x = self.function(previous_n)
            f_x = self.function(n)
            root_in_interval = self.function(
                previous_n) * self.function(n) == 0

            if root_in_interval and iteration == 1:
                print((
                    "Una raiz a la ecuacion dada es "
                    "es uno de los extremos del intervalo"
                ))
                break

            next_n = self.secant_method(previous_n, n)
            f_next_x = self.function(next_n)

            if f_next_x == 0:
                print(f"La raiz del intervalo es {next_n}")
                break

            if iteration > 1:
                error = self.absolute_error(n, next_n)

            row = f"{iteration} \t | {n} | {next_n} | {f_x} | {f_next_x} | {error if error else '' }"
            print(row)

            if error <= self.TOLERANCE and abs(f_next_x) <= self.TOLERANCE:
                print(f"Una raiz aproximada de la ecuación es {next_n}")
                break
                
            n = next_n

            iteration += 1
