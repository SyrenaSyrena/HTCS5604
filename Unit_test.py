import unittest
import Calculation
#this makes the contents of our calculation program available for our unit tests to interact with


class Test_calculation(unittest.TestCase):

    def test_add(self):   #we can make functions to test the various functions of our calculation program
        # here we call the add function from the calculation program with the test case 5,6 and store the result
        actual_result = Calculation.add(5, 6)
        expected_result = 11 #we expect the addition of 5,6 to be 11
        #finally we check to see if the expected result matches the actual
        self.assertEqual(expected_result, actual_result)

    #write another function below to test the power function with the test case 2,3 which result in 8

    def test_power(self):
        actual_result = Calculation.power(2, 3)
        expected_result = 8

        self.assertEqual(expected_result, actual_result)

    def test_multiplication(self):
       actual = Calculation.multiply(10, 12)
       expected = 120
       self.assertEqual(actual, expected)

    def test_division(self):
        actual = Calculation.divide(55, 2)
        expected = 27.5
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()