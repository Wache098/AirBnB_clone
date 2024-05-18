import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_init(self):
        state = State("California")
        self.assertEqual(state.__class__.__name__, "State")
        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()
