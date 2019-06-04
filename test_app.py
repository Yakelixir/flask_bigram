#!/usr/bin/env python

import unittest
from jenkins import app


class TestHello(unittest.TestCase):

    def setUp(self):
        """
        SETUP app
        :return:
        """
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        """
        Check status code & data returned from get.(/)
        : @ host @ route
        : @ host data
        :return:
        """
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        """
        Check status code & data returned from get.(/hello/)
        : @ host @ route
        : @ host data
        :return:
        """
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name(self):
        """
        Check status code & data returned from get.(/hello/simon)
        : @ host @ route
        : @ host data
        :return:
        """
        name = 'Simon'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':

    import xmlrunner

    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()