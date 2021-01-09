"""Main

where all magic beguns
"""

from matrix import Matrix
from vector import Vector
from gauss_jordan_particionado import PartitionedGaussJordan
from doolittle import Doolittle
from secant_method import SecantMethod


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


def prepare_find_root_method():
    """create variables such as interval,
    tolerance and decimal to round
    
    @returns a tuple with interval, tolerance and decimals to round
    """
    interval = []
    tolerance = 0.0
    decimals_to_round = 0
    for i in range(2):
        interval.append(int(input(f"{i + 1}º extremo del intervalo: ")))
    while True:
        try:
            tolerance = int(input("Ingresa el valor de la tolerancia en negativo (e. g.) -5"))
            break
        except TypeError:
            print("Tiene que ser un valor numérico")
            continue
    while True:
        if str(input("¿Quieres redondear el valor?: [y / n]: ")) == "y":
            try:
                decimals_to_round = int(input((
                    "Ingresa el valor de los decimales a redondear en positivo "
                    "(e. g.) 5"
                )))
                break
            except TypeError:
                print("Asegúrate de colocar un valor numérico")
                continue
        else:
            break
    
    return (interval, tolerance, decimals_to_round)
    

def print_menu():
    """Prints the menu"""
    print("\n" * 2, end="")
    print("2. Encontrar una raiz por medio del metodo de la secante")
    print("3. metodo de gauss jordan particionado")
    print("5. factorización por método de Doolittle")
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
        elif option == 2:
            (interval, tolerance, decimal_to_round) = prepare_find_root_method()
            secant = SecantMethod(
                interval[0],
                interval[1],
                tolerance=tolerance,
                decimal_to_round=decimal_to_round
            )
            print(f"Comienza el método para la función {secant.function_name}")
            (axis_x, axis_y) = secant.tabulate(interval=interval)
            secant.plot(axis_x, axis_y)
            secant.solve()
        elif option == 3:
            (matrix, vector) = create_expanded_matrix()
            partitioned_gauss_jordan = PartitionedGaussJordan(matrix.matrix, vector.vector, matrix_name="A", vector_name="b")
            partitioned_gauss_jordan.solve()
        elif option == 5:
            (matrix, vector) = create_expanded_matrix()
            doolittle = Doolittle(matrix=matrix, matrix_name="A", vector=vector, vector_name="b")
            doolittle.solve()
        elif option == 6: print_menu()
    