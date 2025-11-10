import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    #add
    def test_add1(self):
        self.assertEqual(self.calc.add(3,7),10)
    def test_add2(self):
        self.assertEqual(self.calc.add(8,-3),5)
    #subtract
    def test_Subtract1(self):
        self.assertEqual(self.calc.subtract(3,7),-4)
    def test_Subtract2(self):
        self.assertEqual(self.calc.subtract(3,-7),10)
    #multiply
    def test_Mul1(self):
        self.assertEqual(self.calc.multiply(2,5),10)
    def test_Mul2(self):
        self.assertEqual(self.calc.multiply(2,0),0)
    #divide
    def test_divide1(self):
        self.assertEqual(self.calc.divide(6,3),2)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(6,4),1)
    #mod
    def test_Mod1(self):
        self.assertEqual(self.calc.modulo(9,3),0)
    def test_Mod2(self):
        self.assertEqual(self.calc.modulo(6,4),2)
if __name__ == '__main__':
    unittest.main()

