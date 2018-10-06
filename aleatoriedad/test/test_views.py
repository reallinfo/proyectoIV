from django.test import TestCase
from django.urls import reverse

import json

class AleatoriedadViewsTest(TestCase):
    def test_random_number(self):
        res = self.client.get('/random/random_number')
        self.assertEqual(res.status_code, 400)

        res = self.client.get('/random/random_number?max=0&min=0')
        self.assertEqual(res.json()['random_number'], 0)
