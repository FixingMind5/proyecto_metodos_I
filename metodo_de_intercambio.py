"""Swap method module"""
from matrix import Matrix
from vector import Vector
from copy import deepcopy


class SwapMethod:
    """Swap Method Class"""
    matrix = Matrix
    matrix_name = str
    vector = Vector

    def __init__(self, matrix, vector, matrix_name="A", vector_name="b"):
        """Constructor method

        @param matrix: a matrix Object
        @param vector: a vector Object
        @param matrix_name: (Optional) el nombre de la matriz por defecto A
        @param vector_name = (Optional) el nombre del vector
        """
        self.matrix = matrix
        self.vector = vector
        self.matrix_name = matrix_name
        self.vector_name = vector_name

    def greater_pivot(self, values):
        """obtain the grater number in absolute value of the set
        of values
        
        @param values: a list of values
        @return the grater value in list.
        """
        temp_value = 0.0

        for value in values:
            if abs(value) > temp_value:
                temp_value = abs(value)
        
        return temp_value

    def swap(self):
        """swap method
        
        follows the swap method to modify a matrix
        @raise ValueError if matrix not squared
        @returns a Matrix Object
        """
        print("Haz ingresado la matriz: ")
        self.matrix.print_matrix()
        matrix = deepcopy(self.matrix.matrix)
        (index_of_pivot, pivot) = (int, float)
        self.matrix.validate_matrix()
        matrix_end = len(matrix) - 1

        for i in range(len(matrix)):
            pivot = self.greater_pivot(matrix[i])
            index_of_pivot = matrix[i].index(pivot)

            for j in range(len(matrix)):
                if j != index_of_pivot:
                    matrix[i][j] /= pivot * -1

                for k in range(len(matrix[j])):
                    if k != i and j != index_of_pivot:
                        matrix[k][j] += matrix[i][j] * matrix[k][index_of_pivot]

                    is_loop_end = j == matrix_end and k == matrix_end

                for k in range(len(matrix[i])):
                    if is_loop_end:
                        matrix[k][index_of_pivot] /= pivot

            matrix[i][index_of_pivot] = 1 / pivot
        
        return Matrix(matrix)
    
    def solve(self):
        """Solve mehtod
        
        @returns the value of the comprobation
        """
        result_matrix = self.swap()
        print("Matriz resultante:")
        result_matrix.print_matrix()
        sorted_matrix = result_matrix.sort_matrix(self.matrix)
        solution_vector = sorted_matrix.multiply_vector(self.vector)
        solution_vector.set_name("solución")
        solution_vector.print_vector()
        comprobation_value = self.matrix.comprobation(solution_vector.vector)

        return comprobation_value
