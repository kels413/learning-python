from hello import hello


#arrange
#act
#assert


import unittest
#
def add_integers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both numbers should be integers")

    return a + b

class TestAddition(unittest.TestCase):
    """Test addition of integers"""

    def test_add_integers(self):
        # Test case 1
        result1 = add_integers(10, 20)
        self.assertEqual(result1, 30, "Expected result is 30")

        # Test case 2
        result2 = add_integers(-5, 8)
        self.assertEqual(result2, 3, "Expected result is 3")

    def test_add_non_integers(self):
        # Test case 3 (with non-integer inputs)
        with self.assertRaises(ValueError):
            add_integers(3.14, 5)

if __name__ == '__main__':
    unittest.main()

#
# def addSum(a,  b):
#     return a + b
#
#
# class testSum(unittest.TestCase):
#     def test_sum(self):
#         a = 10
#         b = 20
#         result = addSum(10, 10)
#
#         self.assertEqual(result, 20, "Expected 20")
#
#
# if __name__ == "__main__":
#     unittest.main()
#
#
