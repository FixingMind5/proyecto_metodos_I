"""Doolittle method module"""
import copy
from matrix import Matrix
from vector import Vector

class Doolittle:
    """Doolittle method class"""
    matrix = Matrix([])
    vector = Vector([])
    matrix_name = str
    vector_name = str

    def __init__(self, matrix=None, matrix_name="", vector=None, vector_name=""):
        """Dolittle method constructor
        
        @param matrix: must be a Matrix Object
        @param matrix_name: a string with the matrix name
        @param vector: must be a Vector object
        @param vector_name: a string w/ vector name
        """
        self.matrix = matrix
        self.vector = vector
        self.matrix_name = matrix_name
        self.vector_name = vector_name
    
    def verify_sub_matrixes(self, matrix=None):
        """Verify if sub matrixes determinant are != 0

        @param matrix: (Optional) must be a Matrix object
        @returns 
        """
        local_matrix = matrix if matrix else self.matrix

        for i in range(len(local_matrix.matrix)):
            temp_matrix = [[]]
            for j in range(i + 1):
                for k in range(i + 1):
                    temp_matrix[j].append(local_matrix.matrix[j][k])
                temp_matrix.append([])
            
            temp_matrix.remove([])
            submatrix = Matrix(temp_matrix)
            print(f"Submatriz de {i + 1}x{i + 1}")
            det = submatrix.get_determinant()
            print(f"Determinante = {det}")
            submatrix.print_matrix()
            if det == 0:
                return False
        
        return True

    def doolittle_factorization(self, matrix=None):
        """Do LU factorization with doolittle method

        @param matrix: A Matrix Object or an array of arrays
        @returns a tuple with upper and lower factorization
        """
        try:
            local_matrix = self.matrix.matrix if not matrix else matrix.matrix
        except AttributeError:
            local_matrix = matrix
        
        (result, upper, lower, temp_sum) = (0.0, [[]], [[]], 0.0)
        for i in range(len(local_matrix)):
            lower.append([])
            for j in range(len(local_matrix[i])):
                lower[i].append(0)
        
        lower.remove([])

        for i in range(len(local_matrix)):
            for j in range(len(local_matrix[i])):
                temp_sum = 0.0
                for k in range(i):
                    temp_sum += lower[i][k] * upper[k][j]
                result = local_matrix[i][j] - temp_sum
                upper[i].append(round(result, 9))
            upper.append([])
            
            for j in range(len(local_matrix[i])):
                temp_sum = 0.0
                for k in range(i):
                    temp_sum += lower[j][k] * upper[k][i]
                result = local_matrix[j][i] - temp_sum
                lower[j][i] = round(result / upper[i][i], 9)

        upper.remove([])
        upper = Matrix(upper, name="U")
        lower = Matrix(lower, name="L")

        print("Las matrices son: ")
        upper.print_matrix()
        lower.print_matrix()

        print("Al multiplicarlas queda")
        comprobation = lower.multiply_matrix(upper.matrix)
        comprobation.set_name("comprobación de la factorización LU")
        comprobation.print_matrix()

        return (lower, upper)
        
    def solve(self):
        """Solve method

        Starts to run Doolittle method
        
        @returns comprobation
        """
        is_valid = self.verify_sub_matrixes()
        
        if not is_valid:
            raise ValueError((
                "El determinante es igual a cero "
                "el método no puede continuar"
            ))
        
        (lower, upper) = self.doolittle_factorization()

        lower_solution_vector = lower.solve_matrix(matrix=None, vector=self.vector.vector)
        lower_solution_vector.print_vector()
        upper_solution_vector = upper.solve_matrix(
            matrix=None, vector=lower_solution_vector.vector)
        upper_solution_vector.print_vector()

        comprobation = self.matrix.comprobation(upper_solution_vector.vector)
        return comprobation


