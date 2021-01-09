"""Test secant method module"""
from secant_method import SecantMethod


def test_tabulation():
    """test secant.tabulation()"""
    INTERVAL = [-6, 6]
    TOLERANCE = -5
    DECIMAL_TO_ROUND = 5

    secant = SecantMethod(INTERVAL[0], INTERVAL[1], TOLERANCE, decimal_to_round=DECIMAL_TO_ROUND)
    (_, result_list) = secant.tabulate()

    assert result_list is not None


def test_plotting():
    """test secant.plot()"""
    INTERVAL = [-6, 6]
    TOLERANCE = -5

    secant = SecantMethod(INTERVAL[0], INTERVAL[1],
                          TOLERANCE)
    (axis_x, result_list) = secant.tabulate(interval=INTERVAL)

    secant.plot(axis_x, result_list)

def test_solve_method():
    """test secant.solve()"""
    INTERVAL = [0, 0.6]
    TOLERANCE = -5

    secant = SecantMethod(INTERVAL[0], INTERVAL[1], TOLERANCE, 5)
    secant.solve()
