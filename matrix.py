"""Matrix module"""
from vector import Vector

class Matrix:
    """Class Matrix

    holds all the matrixs methods
    @property matrix: an array
    """
    matrix = []
    inverse_matrix = []
    name = ""
    inverse_matrix_name = ""

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

    def print_matrix(self, inverse=False):
        """Prints the element of a matrix
        
        @param param name: A string with the matrix name
        """
        matrix = self.matrix if not inverse else self.inverse_matrix
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
