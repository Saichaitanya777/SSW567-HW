import unittest


def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        return "Right"

    if a == b or a == c or b == c:
        return "Isosceles"

    return "Scalene"


class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(5, 3, 4), "Right")
        self.assertEqual(classify_triangle(4, 5, 3), "Right")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
        self.assertEqual(classify_triangle(3, 4, 3), "Isosceles")
        self.assertEqual(classify_triangle(4, 3, 3), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

    def test_invalid(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid")

    def test_failure_case(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid")


if __name__ == "__main__":
    unittest.main()
