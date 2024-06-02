import unittest
import math



class TestTask(unittest.TestCase):
    def test_no_real_roots(self):
        a = 1
        b = 2
        c = 5
        result = solve_quadratic_equation(a, b, c)
        self.assertEqual(result, [])

    def test_one_real_root(self):
        a = 1
        b = -2
        c = 1
        result = solve_quadratic_equation(a, b, c)
        self.assertEqual(result, [1])

    def test_two_real_roots(self):
        a = 1
        b = -4
        c = 3
        result = solve_quadratic_equation(a, b, c)
        self.assertEqual(result, [1, 3])

    def test_zero_coefficient_a(self):
        a = 0
        b = 2
        c = 1
        with self.assertRaises(ValueError):
            solve_quadratic_equation(a, b, c)


def solve_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент a должен быть не равен 0")
    D = b ** 2 - 4 * a * c
    if D < 0:
        return []
    if D == 0:
        x1 = -(b) / (2 * a)
        return [x1]
    if D > 0:
        x1 = (-(b) - math.sqrt(D)) / (2 * a)
        x2 = (-(b) + math.sqrt(D)) / (2 * a)
        return [x1, x2]


if __name__ == '__main__':
    unittest.main()
