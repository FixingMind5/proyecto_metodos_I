"""Test matrix determinant module"""
from matrix import Matrix

def test_get_2x2_determinant_method():
    """tests get 2x2 determinant method"""
    matrix = Matrix([
        [4, 5],
        [5, 8],
    ])
    det = matrix.get_determinant()

    assert det == 7


def test_get_3x3_determinant_method():
    """tests get 3x3 determinant method"""
    matrix = Matrix([
        [4, 5, 2],
        [5, 8, 7],
        [3, 7, -4]
    ])
    det = matrix.get_determinant()

    assert det == -97


def test_get_4x4_determinant_method():
    """tests get 4x4 determinant method"""
    matrix = Matrix([
        [4, 5, 2, -1],
        [5, 8, 7, 6],
        [3, 7, -4, -2],
        [-1, 6, -2, 5]
    ])
    det = matrix.get_determinant()

    assert det == 378
