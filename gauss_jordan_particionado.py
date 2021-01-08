"""Partitioned Gauss-Jordan method"""
from matrix import Matrix
from vector import Vector
import copy

class PartitionedGaussJordan:
    """Partitioned Gauss Jordan method
    
    use solve() to run the process
    """
    matrix = []
    vector = []

    def __init__(self, matrix, vector, matrix_name="", vector_name=""):
        """Partitioned Gauss Jordan constructor
        
        @param param matrix: An array of arrays
        @param param vector: An array
        """
        self.matrix = Matrix(matrix)
        self.vector = Vector(vector)

        self.matrix.set_name(matrix_name)
        self.vector.set_name(vector_name)

    def solve(self):
        """Solve a 4x4 matrix using the method
        
        @param param matrix: The coeficients matrix of the exercise
        @param param vector: The solution vector of the exercise
        """

        # Begins parititons
        matrix = copy.deepcopy(self.matrix.matrix)
        vector = copy.deepcopy(self.vector.vector)
        print("Comienza las particiones")
        a_11 = Matrix([
            [matrix[0][0], matrix[0][1]], 
            [matrix[1][0], matrix[1][1]]
        ], name="a_11")
        a_11.print_matrix()
        a_12 = Matrix([
            [matrix[0][2], matrix[0][3]],
            [matrix[1][2], matrix[1][3]]
        ], name="a_12")
        a_12.print_matrix()
        a_21 = Matrix([
            [matrix[2][0], matrix[2][1]],
            [matrix[3][0], matrix[3][1]]
        ], name="a_21")
        a_21.print_matrix()
        a_22 = Matrix([
            [matrix[2][2], matrix[2][3]],
            [matrix[3][2], matrix[3][3]]
        ], name="a_22")
        a_22.print_matrix()

        # Obteniendo los vectores
        print(f"Obteniendo las particiones del vector {self.vector.name}")
        b_1 = Vector([vector[0], vector[1]], name="b_1")
        b_2 = Vector([vector[2], vector[3]], name="b_2")
        b_1.print_vector()
        b_2.print_vector()

        # Empieza las sustituciones con matrices de identidad
        print("Sustituyendo a_11 con la matriz identidad de 2x2")
        (matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]) = (1.0, 0.0, 0.0, 1.0)
        print("Así va quedando la matriz")
        self.matrix.print_matrix(matrix=matrix)

        # Hallando la matriz inversa de a_11
        print("Hallando a_11 prima")
        a_11.find_inverse_matrix()
        a_11.print_matrix(inverse=True)

        # Hallando a_12 prima
        print("Hallando a_12 prima")
        a_12_prime = a_11.multiply_matrix(a_12.matrix, inverse=True)
        a_12.set_name("a_12 prima")
        a_12_prime.print_matrix()

        # Obteniendo b_1 prima
        print("Obteniendo vector b_1 prima")
        b_1_prime = a_11.multiply_vector(b_1, inverse=True)
        b_1.set_name("b_1 prima")
        b_1_prime.print_vector()

        # Substituyendo los valores de la partitcion a_12 con los de la particion a_12_prima
        print("Substituyendo los valores de a_12 con los de a_12_prima")
        (matrix[0][2], matrix[0][3], matrix[1][2], matrix[1][3]) = (a_12_prime.matrix[0][0], a_12_prime.matrix[0][1], a_12_prime.matrix[1][0], a_12_prime.matrix[1][1])
        self.matrix.print_matrix(matrix=matrix)

        # Subsituyendo los valores de la particion b_1 del vector solucion
        # con los valores de b_1 prima
        (vector[0], vector[1]) = (b_1_prime.vector[0], b_1_prime.vector[1])
        print("Vector solucion")
        self.vector.print_vector(vector=vector)

        print("Obteniendo a_22 prima")
        a_22_prime = a_22.minus_matrix(a_21.multiply_matrix(a_12_prime.matrix).matrix)
        a_22_prime.set_name("a_22 prima")
        a_22_prime.print_matrix()
        print("Obteniendo b_2")
        b_2_prime = b_2.minus_vector(a_21.multiply_vector(b_1_prime))
        b_2_prime.print_vector()

        # intercambiando las particiones
        print("Intercambiando la particion a_21 con una matriz de ceros")
        (matrix[2][0], matrix[2][1], matrix[3][0], matrix[3][1]) = (0, 0, 0, 0)
        print("Intercambiando la particion a_22 con a_22 prima")
        (matrix[2][2], matrix[2][3], matrix[3][2], matrix[3][3]) = (a_22_prime.matrix[0][0], a_22_prime.matrix[0][1], a_22_prime.matrix[1][0], a_22_prime.matrix[1][1])
        (vector[2], vector[3]) = (b_2_prime.vector[0], b_2_prime.vector[1])
        print("Así queda la matriz")
        self.matrix.print_matrix(matrix=matrix)
        print("Asi queda el vector solucion")
        self.vector.print_vector(vector=vector)

        # Obteniendo la prima de a_22 y c_2
        print("Obteniendo la particion a_22")
        a_22_prime.find_inverse_matrix()
        a_22_prime.print_matrix()
        print("obteniendo el vector c_2")
        c_2 = a_22_prime.multiply_vector(b_2_prime, inverse=True)
        c_2.print_vector()

        # Intercambiando las particiones
        print("Intercambiando las particiones")
        (matrix[2][2], matrix[2][3], matrix[3][2], matrix[3][3]) = (1.0, 0.0, 0.0, 1.0)
        (vector[2], vector[3]) = (c_2.vector[0], c_2.vector[1])
        print("Nuestra matriz principal:")
        self.matrix.print_matrix(matrix=matrix)
        print("Nuestro vector solucion")
        self.vector.print_vector(vector=vector)

        # Encontrando la particion c_1
        print("Encontrando la particion c_1")
        c_1 = b_1_prime.minus_vector(a_12_prime.multiply_vector(c_2))
        c_1.print_vector()

        # Intercambiando las particiones
        (matrix[0][2], matrix[0][3], matrix[1][2], matrix[1][3]) = (0.0, 0.0, 0.0, 0.0)
        (vector[0], vector[1]) = (c_1.vector[0], c_1.vector[1])
        print("Finalmente la matriz queda como")
        self.matrix.print_matrix(matrix=matrix)
        print("Y el vector solucion como")
        self.vector.print_vector(vector=vector)
        print("\n" * 3, end="")

        self.matrix.comprobation(vector)