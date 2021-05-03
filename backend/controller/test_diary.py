import unittest
import sys
import io
import os

from app import app


class TestDiary(unittest.TestCase):
    def setUp(self):
        print('Test Diary')
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        print('End Test')

    def test_register_diary(self):
        res = self.client.post('/diary', json={})
        self.assertEqual(res.status_code, 400)

        res = self.client.post('/diary', json={'title': ''})
        self.assertEqual(res.status_code, 400)

        res = self.client.post(
            '/diary', json={'title': 'title', 'content': '', 'user_id': 0})
        self.assertEqual(res.status_code, 400)
