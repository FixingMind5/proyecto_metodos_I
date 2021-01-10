"""Test swap method module"""
from metodo_de_intercambio import SwapMethod
from matrix import Matrix
from vector import Vector


def test_solve():
    """tests swap.solve()"""
    matrix = Matrix([
        [1, 2],
        [2, 1]
    ])
    vector = Vector([3, 2])
    swap = SwapMethod(matrix, vector)
    result_matrix = swap.swap()
    correct_matrix = [
        [-1 * 1/3, 2/3],
        [2/3, -1 * 1/3]
    ]

    assert result_matrix == correct_matrix


def test_solving():
    """test swap.solve()"""
    matrix = Matrix([
        [1, 2, 1],
        [1, 1, 2],
        [2, 1, 1]
    ])
    vector = Vector([3, 2, 1])
    swap = SwapMethod(matrix, vector)
    comprobation = swap.solve()

    assert comprobation == 3
