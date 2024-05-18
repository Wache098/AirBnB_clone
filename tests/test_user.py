import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_init(self):
        user = User("test_user")
        self.assertEqual(user.__class__.__name__, "User")
        self.assertEqual(user.username, "test_user")

if __name__ == '__main__':
    unittest.main()
