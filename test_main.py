import unittest
from main import add  # Importe la fonction add depuis main.py

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test que 2 + 3 = 5

if __name__ == '__main__':
    unittest.main()
