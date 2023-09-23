#!/user_id/bin/env python


__author__ = "Sai Chaitanya"

import unittest

from hw2.Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    """
    define multiple sets of tests as functions with names that begin
    """
    # Testing Equilateral Triangles
    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testEquilateralTriangle2(self):
        self.assertEqual(classifyTriangle(27, 27, 27), 'Equilateral')

    def testEquilateralTriangle3(self):
        self.assertNotEqual(classifyTriangle(17, 20, 10), 'Equilateral')

    # Testing Isosceles Triangles
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(7, 7, 3), 'Isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(5, 9, 9), 'Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(7, 5, 7), 'Isosceles')

    def testIsoscelesTriangle4(self):
        self.assertEqual(classifyTriangle(8, 8, 6), 'Isosceles')

     # Testing Right Triangles
    def testRightTriangle1(self):
            self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangle2(self):
            self.assertEqual(classifyTriangle(4, 3, 5), 'Right')

    def testRightTriangle3(self):
            self.assertEqual(classifyTriangle(12, 13, 5), 'Right')

    def testRightTriangle4(self):
        self.assertEqual(classifyTriangle(6, 10, 8), 'Right')

    def testRightTriangle5(self):
        self.assertNotEqual(classifyTriangle(12, 6, 10), 'Right')

    # Testing Scalene Triangles
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(11, 10, 12), 'Scalene')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(6, 4, 3), 'Scalene')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(41, 50, 90), 'Scalene')

    def testScaleneTriangle4(self):
        self.assertNotEqual(classifyTriangle(60, 60, 90), 'Scalene')

    # Testing Invalid Inputs
    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(-10, -11, -16), 'InvalidInput')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle("0", "0", "0"), 'InvalidInput')

    # Testing Not a Triangle
    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(5, 2, 1), 'NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(3, 5, 1), 'NotATriangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(1, 5, 1), 'NotATriangle')

    def testNotATriangle4(self):
        self.assertEqual(classifyTriangle(1, 10, 5), 'NotATriangle')



if __name__ == '__main__':
    print('--------------Starting Unit Tests--------------')
    unittest.main()
