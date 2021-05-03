import unittest
import sys
import io
import os

from app import app


class TestTopic(unittest.TestCase):
    def setUp(self):
        print('Test Topic')
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        print('End Test')

    def test_register_diary(self):
        res = self.client.post('/topic', json={})
        self.assertEqual(res.status_code, 400)

        res = self.client.post('/topic', json={'name': 'name'})
        self.assertEqual(res.status_code, 400)

        res = self.client.post(
            '/topic', json={'name': '', 'user_id': 0})
        self.assertEqual(res.status_code, 400)
