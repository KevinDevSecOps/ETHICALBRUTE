import unittest
from src.password_checker import check_password

class TestPasswordChecker(unittest.TestCase):
    def test_check_password(self):
        self.assertTrue(check_password("123", "123"))
        self.assertFalse(check_password("123", "456"))

if __name__ == "__main__":
    unittest.main()
