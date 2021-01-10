"""Test swap method module"""
from metodo_de_intercambio import SwapMethod
from matrix import Matrix
from vector import Vector


def test_swap():
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


def test_2x2_solving():
    """tests swap.solve()"""
    matrix = Matrix([
        [1, 2],
        [2, 1]
    ])
    vector = Vector([3, 2])
    swap = SwapMethod(matrix, vector)
    comprobation = swap.solve()

    assert comprobation == 3


def test_3x3_solving():
    """test swap.solve()"""
    matrix = Matrix([
        [3, 2, 1],
        [5, 3, 4],
        [1, 1, -1]
    ])
    vector = Vector([1, 2, 1])
    swap = SwapMethod(matrix, vector)
    comprobation = swap.solve()

    assert comprobation == 1


def test_4x4_solving():
    """test swap.solve()"""
    matrix = Matrix([
        [3, 6, -2, 9],
        [-5, 4, 5, -6],
        [-3, 8, 2, -3],
        [-4, 10, 3, 9]
    ])
    vector = Vector([6, 5, 3, 9])
    swap = SwapMethod(matrix, vector)
    comprobation = swap.solve()

    assert comprobation == 6
