import unittest
import sys
import io
import os

from app import app


class TestUser(unittest.TestCase):
    def setUp(self):
        print('Test User')
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        print('End Test')

    def test_register_diary(self):
        res = self.client.post('/user', json={})
        self.assertEqual(res.status_code, 400)

        res = self.client.post('/user', json={'name': ''})
        self.assertEqual(res.status_code, 400)
