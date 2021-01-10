"""Test dolittle submatrixes verification"""
from matrix import Matrix
from doolittle import Doolittle
from vector import Vector


def test_submatrixes():
    """Verify if the method of submatrixes works"""
    matrix = Matrix([
        [4, 5, 2, -1],
        [5, 8, 7, 6],
        [3, 7, -4, -2],
        [-1, 6, -2, 5]
    ])
    doolittle = Doolittle(matrix=matrix, matrix_name="A")
    is_valid = doolittle.verify_sub_matrixes()

    assert is_valid == True

def test_lu_factorization():
    """Tests if LU factorization works"""
    matrix = Matrix([
        [4, 5, 2, -1],
        [5, 8, 7, 6],
        [3, 7, -4, -2],
        [-1, 6, -2, 5]
    ])
    vector = Vector([3, 2, 0, 1])
    doolittle = Doolittle(matrix=matrix, matrix_name="A", vector=vector, vector_name="b")
    doolittle.solve()


def test_solve_3x3():
    """Tests if LU factorization works"""
    matrix = Matrix([
        [5, -3, -1],
        [1, 4, -6],
        [2, 3, 4]
    ])
    vector = Vector([1, -1, 9])
    doolittle = Doolittle(matrix=matrix, matrix_name="A",
                          vector=vector, vector_name="b")
    comprobation = doolittle.solve()

    assert comprobation == 1


def test_solve_4x4():
    """Tests if LU factorization works"""
    matrix = Matrix([
        [1, -2, 2, -3],
        [3, 4, -1, 1],
        [2, -3, 2, -1],
        [1, 1, -3, -2]
    ])
    vector = Vector([15, -6, 17, -7])
    doolittle = Doolittle(matrix=matrix, matrix_name="A",
                          vector=vector, vector_name="b")
    comprobation = doolittle.solve()

    assert comprobation == 15
