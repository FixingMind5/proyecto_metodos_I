from matrix import Matrix
from vector import Vector
from gauss_jordan_particionado import PartitionedGaussJordan
from doolittle import Doolittle


def create_expanded_matrix():
    """Creates matrix and vector needed in order to
    continue with the methods
    """
    vector = Vector([])
    matrix = Matrix([])
    print("Comienza la creacion de la matriz")
    matrix.create_matrix()
    print("Comienza la creacion del vector")
    vector.create_vector()

    return (matrix, vector)


def print_menu():
    """Prints the menu"""
    print("\n" * 2, end="")
    print("1. metodo de gauss jordan particionado")
    print("3. factorización por método de Doolittle")
    print("0. Salir")
    print()

if __name__ == "__main__":
    print("Proyecto final de metodos numericos")
    print("A continuación seleccione la opción que usará")
    print_menu()

    while True:
        print("Para volver a ver el menú escriba 6")
        option = int(input("Eliga una opcion: "))
        
        if option < 0 or option > 6:
            print("Opcion invalida intente de nuevo")
        
        if option == 0:
            print("Bye ;)")
            break
        elif option == 1:
            (matrix, vector) = create_expanded_matrix()
            partitioned_gauss_jordan = PartitionedGaussJordan(matrix.matrix, vector.vector, matrix_name="A", vector_name="b")
            partitioned_gauss_jordan.solve()
        elif option == 3:
            (matrix, vector) = create_expanded_matrix()
            doolittle = Doolittle(matrix=matrix, matrix_name="A", vector=vector, vector_name="b")
            doolittle.solve()
        elif option == 6:
            print_menu()
    
