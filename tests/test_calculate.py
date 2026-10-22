import unittest
from ArithmeticCalculator import calculate


class UnitTests(unittest.TestCase):
    def test_example(self):
        self.assertNotEqual('foo'.upper(), 'foo')
        print("Running test case...")

    def test_calculator_add(self):
        data = {
            "num1": 4,
            "num2": 3,
            "opt": "+"
        }
        result = calculate(data)
        print("Result ", result["data"]["result"])
        self.assertEqual(result["data"]["result"], 7)

    def test_calculator_subtract(self):
        data = {
            "num1": 4,
            "num2": 3,
            "opt": "-"
        }
        result = calculate(data)
        print("Result ", result["data"]["result"])
        self.assertEqual(result["data"]["result"], 1)

    def test_calculator_multiply(self):
        data = {
            "num1": 4,
            "num2": 3,
            "opt": "*"
        }
        result = calculate(data)
        print("Result ", result["data"]["result"])
        self.assertEqual(result["data"]["result"], 12)

    def test_calculator_divide(self):
        data = {
            "num1": 4,
            "num2": 4,
            "opt": "/"
        }
        result = calculate(data)
        print("Result ", result["data"]["result"])
        self.assertEqual(result["data"]["result"], 1)

    def test_calculator_division_by_zero(self):
        data = {
            "num1": 3,
            "num2": 0,
            "opt": "/"
        }
        result = calculate(data)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
