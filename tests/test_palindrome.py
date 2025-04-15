from src.palindrome import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome("AcA")
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome("ABCA")
        self.assertEqual(resultado, False)


    def test_e(self):
        resultado = is_palindrome("Anita lava la tina")
        self.assertEqual(resultado, True)
    

if __name__ == '__main__':
    unittest.main()