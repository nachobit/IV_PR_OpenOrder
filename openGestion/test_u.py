import unittest
from app import app
from flask import Flask, render_template

def fun(x):
    return x + 1

class TestCode(unittest.TestCase):
    def test_code(self):
        self.test_app = app.test_client()
        
        #Test demo
        self.assertEqual(fun(3), 4)

        #Test Response is 200 OK
        response = self.test_app.get('/gestion', follow_redirects=True)
        self.assertEqual(response.status, "200 OK")

        # Test logging out
        logout = self.test_app.get('/logout', follow_redirects=True)
        #assert 'You were logged out' in logout.data

if __name__ == '__main__':
    unittest.main()