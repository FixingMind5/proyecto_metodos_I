"""Matrix module"""
from vector import Vector
import copy

class Matrix:
    """Class Matrix

    holds all the matrixs methods
    @property matrix: an array
    """
    matrix = []
    inverse_matrix = []
    name = ""
    inverse_matrix_name = ""
    det = 0

    def __init__(self, matrix, name=""):
        """Init for a matrix gived
        
        @param param matrix: could be a Matrix object or
        an array of arrays
        """
        self.matrix = matrix
        self.name = name
    
    def set_name(self, name):
        """Assign a name if any given
        
        @param param name: A string
        @raise TypeError if name isn't a string
        """
        if type(name) is not str:
            raise TypeError("El nombre debe de ser una string")

        self.name = name

    def create_matrix(self):
        """Creates a matrix of 4x4 with values
        gived by the user"""
        user_input = float

        print("Ingresa los coeficientes correspondientes")
        for i in range(4):
            is_vector_valid = bool
            temp_vector = Vector([])
            for j in range(4):
                try:
                    user_input = float(input(f"A[{i + 1}][{j + 1}] = "))
                except ValueError:
                    print("Asegurate de ingresar un valor numerico")
                    break

                temp_vector.vector.append(user_input)
            
            is_vector_valid = temp_vector.validate_vector()

            if is_vector_valid:
                self.matrix.append(temp_vector.vector)

        print("\n" * 3, end="")
        print("Fin del llenado de valores")
        print("\n" * 3, end="")
        self.print_matrix()

    def validate_matrix(self):
        """Validates if matrix is squared.
        
        @raise ValueError if matrix not squared
        """

        if len(self.matrix[0]) != len(self.matrix):
            raise ValueError("La matriz debe de ser cuadrada")

    def print_matrix(self, matrix=None, inverse=False):
        """Prints the element of a matrix
        
        @param param name: A string with the matrix name
        """
        matrix = self.matrix if not matrix else matrix

        if inverse:
            matrix = self.inverse_matrix

        name = self.name if not inverse else self.inverse_matrix_name

        print(f"Matriz {name}")
        for i in range(len(matrix)):
            print("|", end="")
            for j in range(len(matrix[i])):
                print(f"{matrix[i][j]}", end=" ")
            print("|")

        print("\n" * 3, end="")

    def multiply_matrix(self, matrix, inverse=False):
        """Multiply two matrix

        @param param matrix: it could be Matrix objecto
        or an array of arrays
        @param param inverse: Bool, default is false

        @raise ValueError if matrix couldn't be multiplied

        @returns a Matrix Object
        """
        temp_matrix = [[]]
        local_matrix = self.matrix if not inverse else self.inverse_matrix

        if not (len(local_matrix[0]) == len(matrix)):
            raise ValueError((
                "El renglon de la primera matriz "
                "no es del mismo tamaño a la columna "
                "de la segunda matriz"
            ))

        for i in range(len(local_matrix)):
            for j in range(len(local_matrix[i])):
                temp_value = 0.0
                for k in range(len(matrix)):
                    temp_value += local_matrix[i][k] * matrix[k][j]
                temp_matrix[i].append(temp_value)
            temp_matrix.append([])

        temp_matrix.remove([])

        return Matrix(temp_matrix)

    def multiply_vector(self, vector, inverse=False):
        """Multiply a matrix times vector

        @param param vector: a list
        @returns a vector"""
        temp_vector = []
        matrix = self.inverse_matrix if inverse else self.matrix

        for i in range(len(matrix)):
            temp_value = 0.0
            for j in range(len(matrix[i])):
                temp_value += matrix[i][j] * vector.vector[j]
            temp_vector.append(temp_value)

        return Vector(temp_vector)

    def find_inverse_matrix(self):
        """Calculate the inverse matrix of a given 4x4
        matrix

        @param param name: The name you want for the matrix
        @raise ZeroDivisionError if det = 0
        """
        det = (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
        if det == 0:
            raise ZeroDivisionError((
                "El determinante de la matriz es cero "
                "lo que causara que calcular su matriz inversa "
                "falle."
            ))
        adjoint_transpose_matrix = [
            [self.matrix[1][1], -1 * self.matrix[0][1]],
            [-1 * self.matrix[1][0], self.matrix[0][0]]
        ]

        print(f"Calculando la matriz inversa de particion {self.name}")
        for i in range(len(adjoint_transpose_matrix)):
            for j in range(len(adjoint_transpose_matrix[i])):
                adjoint_transpose_matrix[i][j] /= det

        print("\n", end="")
        self.inverse_matrix_name = self.name + " inversa"
        self.inverse_matrix = adjoint_transpose_matrix

    def minus_matrix(self, matrix, inverse=False):
        """it reduces two matrixs
        
        @param param matrix: could be an array of arrays [[]]
        or a Matrix object
        @returns a Matrix object
        """
        temp_matrix = [[]]
        local_matrix = self.matrix if not inverse else self.inverse_matrix

        for i in range(len(local_matrix)):
            temp_value = 0.0
            for j in range(len(local_matrix[i])):
                temp_value = local_matrix[i][j] - matrix[i][j]
                temp_matrix[i].append(temp_value)
            temp_matrix.append([])

        temp_matrix.remove([])
        
        return Matrix(temp_matrix)
    
    def get_determinant(self, matrix=None):
        """Obtains the determinant of a given matrix
        
        @param matrix: an array of arrays [[]]
        """
        (sign, det) = (-1, 0)
        temp_matrix = [[]]

        if not matrix:
            matrix = copy.deepcopy(self.matrix)

        if len(matrix) == 2 and len(matrix[0]) == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0]

        for element in matrix[0]:
            sign *= -1
            temp_matrix = copy.deepcopy(matrix)
            index_of_element = matrix[0].index(element)
            for index in range(len(matrix)):
                temp_matrix[index].remove(temp_matrix[index][index_of_element])
            temp_matrix.remove(temp_matrix[0])
            det += (sign * element) * self.get_determinant(temp_matrix)

        return det

    def solve_matrix(self, matrix, vector):
        """Solve a equation system with cramer method

        @param matrix: (Optional) must be an array of arrays [[]]
        if matrix is self, do matrix=None
        @param vector: must be a list
        @raise ValueError if determinant equals to 0
        @returns a Vector Object with the value of the variables
        """
        local_matrix = matrix if matrix else copy.deepcopy(self.matrix)
        solution_vector = []
        temp_det = 0.0
        
        det_A = self.get_determinant()
        if det_A == 0:
            raise ZeroDivisionError((
                "El determinante de la matriz es igual a cero "
                "lo cual dará un error de división por cero."
            ))
        
        for i in range(len(local_matrix)):
            temp_matrix = copy.deepcopy(local_matrix)
            for j in range(len(local_matrix[i])):
                temp_matrix[j][i] = vector[j]
            else:
                temp_det = Matrix(temp_matrix).get_determinant()
                solution_vector.append(temp_det / det_A)

        return Vector(solution_vector, name=f" solucion de la matriz {self.name}")
    
    def comprobation(self, solution_vector):
        """Prints the comprobation of the vector solution
        with the original matrix

        @param solution_vector: an array with the values
        """
        comprobation = 0.0

        for i in range(len(solution_vector)):
            comprobation += self.matrix[0][i] * solution_vector[i]

        print(f"Comprobación: {comprobation}")
