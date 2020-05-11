import unittest

from app import app,BOOKS
from flask import json

class BasicTestCase(unittest.TestCase):

    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/ping', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'"pong!"\n')

    def test_books(self):
        tester = app.test_client(self)
        response = tester.get('/books', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        books_response = json.loads(response.data)
        self.assertIsNotNone(books_response)
        self.assertEqual(books_response['books'], BOOKS)
        


    
if __name__ == '__main__':
    unittest.main()