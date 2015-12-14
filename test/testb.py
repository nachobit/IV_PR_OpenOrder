import unittest
from openGestion import app, db

class TestCode(unittest.TestCase):

	# Ensure that welcome page loads
    def test_welcome(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Welcome!', response.data)

    def test_code(self):
        self.test_app = app.test_client()

if __name__ == '__main__':
    unittest.main()