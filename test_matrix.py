"""Matrix tests module"""
from matrix import Matrix
from gauss_jordan_particionado import PartitionedGaussJordan

def test_matrix_solving():
    """Tests matrix.solve_matrix() method"""
    matrix = Matrix([
        [4, 5, 2, -1],
        [5, 8, 7, 6],
        [3, 7, -4, -2],
        [-1, 6, -2, 5]
    ])
    vector = [3, 2, 0, 1]
    solution_vector = matrix.solve_matrix(matrix=None, vector=vector)
    exercise_solution_vector = [3, -1.75, 1, 7.546391753]

    for index in range(len(solution_vector)):
        assert solution_vector.vector[index] == exercise_solution_vector[index]


def test_partitioned_gauss_jordan():
    """Test if partitioned gauss jordan works"""
    matrix = Matrix([
        [4, 5, 2, -1],
        [5, 8, 7, 6],
        [3, 7, -4, -2],
        [-1, 6, -2, 5]
    ])
    vector = [3, 2, 0, 1]
    partitioned_gauss_jordan = PartitionedGaussJordan(matrix.matrix, vector, matrix_name="A", vector_name="b")
    partitioned_gauss_jordan.solve()