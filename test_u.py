import unittest
from openGestion import app
from flask import Flask, render_template

def fun(x):
    return x + 1

class TestCode(unittest.TestCase):
    def test_code(self):
        self.test_app = app.test_client()
        
        #Test demo
        self.assertEqual(fun(3), 4)

        Test Response is 200 OK
        response = self.test_app.get('/register', follow_redirects=True)
        self.assertEqual(response.status, "200 OK")

        # Test logging out
        logout = self.test_app.get('/logout', follow_redirects=True)
        #assert 'You were logged out' in logout.data

    # Verify that welcome page loads
    #def test_welcome(self):
    #    response = self.client.get('/', follow_redirects=True)
    #    self.assertIn(b'Welcome to Flask!', response.data)

if __name__ == '__main__':
    unittest.main()