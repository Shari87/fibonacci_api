"""
Test the FibonacciServer module
"""

import unittest
from fibonacci_api.fibonacci_server import FibonacciServer


class FibonacciServerTest(unittest.TestCase):

    def setUp(self):
        self.app = FibonacciServer().test_client()

    def test_index(self):
        rv = self.app.get('/health')
        self.assertTrue(rv.status.startswith('200 '))
        self.assertEqual(rv.headers['content-type'],
                         'text/plain; charset=utf-8')
        self.assertTrue(rv.data.startswith(b'Welcome'))

    def test_invalid_index(self):
        rv = self.app.get('/HEALTH')
        self.assertTrue(rv.status.startswith('404 '))
        self.assertTrue(rv.data.startswith(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">'))


    def test_fib_invalid_version(self):
        rv = self.app.get('/fib/0/0')
        self.assertFalse(rv.status.startswith('501 '))

    def test_fib_not_a_number(self):
        rv = self.app.get('/fib/xxx')
        self.assertTrue(rv.status.startswith('404 '))

    def test_fib_float_number(self):
        rv = self.app.get('/fib/0/1.0')
        self.assertTrue(rv.status.startswith('400 '))

    def test_fib_negative_number(self):
        rv = self.app.get('/fib/0/-1')
        self.assertTrue(rv.status.startswith('400 '))

    def test_fib_overflowed_number(self):
        rv = self.app.get('/fib/0/99999999999999')
        self.assertTrue(rv.status.startswith('413 '))

    def test_fib_zero(self):
        rv = self.app.get('/fib/0/0')
        self.assertTrue(rv.status.startswith('200 '))
        self.assertEqual(rv.data, b'[]')

    def test_fib_normal(self):
        rv = self.app.get('/fib/0/2')
        self.assertTrue(rv.status.startswith('200 '))
        self.assertEqual(rv.headers['content-type'], 'application/json')
        self.assertEqual(rv.data, b'[0, 1]')


if __name__ == '__main__':
    unittest.main()