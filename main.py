from matrix import Matrix
from vector import Vector
from gauss_jordan_particionado import PartitionedGaussJordan

if __name__ == "__main__":
    print("Proyecto final de metodos numericos")
    print("A continuación seleccione la opción que usará")
    print("\n")
    print("1. metodo de gauss jordan particionado")
    print("0. Salir")

    while True:
        option = int(input("Eliga una opcion: "))
        
        if option < 0 or option > 1:
            print("Opcion invalida intente de nuevo")
        
        if option == 0:
            print("Bye ;)")
            break
        
        if option == 1:
            vector = Vector([])
            matrix = Matrix([])
            print("Comienza la creacion de la matriz")
            matrix.create_matrix()
            print("Comienza la creacion del vector")
            vector.create_vector()
            partitioned_gauss_jordan = PartitionedGaussJordan(matrix.matrix, vector.vector, matrix_name="A", vector_name="b")
            partitioned_gauss_jordan.solve()

    