"""Main

where all magic beguns
"""
from matrix import Matrix
from vector import Vector
from gauss_jordan_particionado import PartitionedGaussJordan
from doolittle import Doolittle
from secant_method import SecantMethod
from newton_method import NewtonMethod
from metodo_de_intercambio  import SwapMethod


FUNCTION_NAME = "f(x) = cos(x) - x"


def create_expanded_matrix():
    """Creates matrix and vector needed in order to
    continue with the methods

    @returns a tuple with a Matrix object and a Vector object
    in that order: (Matrix, Vector)
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
        interval.append(float(input(f"{i + 1}º extremo del intervalo: ")))
    while True:
        try:
            tolerance = int(input("Ingresa el valor de la tolerancia en negativo (e. g: -5): "))
            break
        except TypeError:
            print("Tiene que ser un valor numérico")
            continue
    while True:
        if str(input("¿Quieres redondear el valor?: [y / n]: ")) == "y":
            try:
                decimals_to_round = int(input((
                    "Ingresa el valor de los decimales a redondear en positivo "
                    "(e. g: 5): "
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
    print("1. Encontrar una raiz por medio del metodo de Newton")
    print("2. Encontrar una raiz por medio del metodo de la secante")
    print("3. metodo de gauss jordan particionado")
    print("4. Resolver una matriz por el método de intercambio")
    print("5. factorización por método de Doolittle")
    print("0. Salir")
    print()

if __name__ == "__main__":
    print("Proyecto final de metodos numericos")
    print("A continuación seleccione la opción que usará")
    print_menu()

    while True:
        print("\n" * 3)
        print("Para volver a ver el menú escriba 6")
        option = int(input("Eliga una opcion: "))
        
        if option < 0 or option > 6:
            print("Opcion invalida intente de nuevo")
        
        if option == 0:
            print("Bye ;)")
            break
        elif option == 1:
            print((
                f"Comienza el método de Newton para la función {FUNCTION_NAME}"
            ))
            (interval, tolerance, decimal_to_round) = prepare_find_root_method()
            value = float(input("Ingresa el valor inicial (debe ser un número): "))
            newton = NewtonMethod(
                value,
                tolerance,
                decimal_to_round
            )
            (axis_x, axis_y) = newton.tabulate(interval=interval)
            newton.plot(axis_x, axis_y)
            newton.solve()
            print("\n")
            print("Conclusión:")
            print((
                "Este método como el de la secante es muy exacto \n"
                "como es de suponer, mientras más tolerancia le \n"
                "permitas, más exacto es el valor de la raíz aunque \n"
                "a veces el valor es tan pequeño que depende de la situación \n"
                "puedes despreciar esa pequeña \"variación\""
            ))
        elif option == 2:
            print((
                f"Comienza el método de Secante para la función {FUNCTION_NAME}"
            ))
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
            print("\n")
            print("Conclusión")
            print((
                "Nuevamente, este método es tan eficiente que el de \n"
                "Newton con respecto a la tolerancia, lo mismo, depende del \n"
                "caso en el que se use puedes permitirte más tolerancia y el error \n"
                "será más pequeño aunque en algunas funciones cabe destacar que a más \n"
                "iteraciones, más probable es que se pierda la raíz así que hay que \n"
                "tener cuidado en ese aspecto"
            ))
        elif option == 3:
            (matrix, vector) = create_expanded_matrix()
            partitioned_gauss_jordan = PartitionedGaussJordan(matrix.matrix, vector.vector, matrix_name="A", vector_name="b")
            partitioned_gauss_jordan.solve()
        elif option == 4:
            (matrix, vector) = create_expanded_matrix()
            swap = SwapMethod(matrix, vector)
            swap.solve()
        elif option == 5:
            (matrix, vector) = create_expanded_matrix()
            doolittle = Doolittle(matrix=matrix, matrix_name="A", vector=vector, vector_name="b")
            doolittle.solve()
        elif option == 6: print_menu()
    