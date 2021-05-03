import unittest
import sys
import io
import os

from app import app


class TestSituationType(unittest.TestCase):
    def setUp(self):
        print('Test Situation Type')
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        print('End Test')

    def test_register_diary(self):
        res = self.client.post('/situation_type', json={})
        self.assertEqual(res.status_code, 400)

        res = self.client.post('/situation_type', json={'name': ''})
        self.assertEqual(res.status_code, 400)
