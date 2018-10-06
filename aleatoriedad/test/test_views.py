from django.test import TestCase
from django.urls import reverse

import json

class AleatoriedadViewsTest(TestCase):
    def test_random_number(self):
        print('Probando La vista de números aleatorios')
        print('Probando resultado con bad input')
        res = self.client.get('/random/random_number')
        self.assertEqual(res.status_code, 400, 'El código devuelto por el servidor no es el esperado')

        print('Porbando resultado con valores válidos')
        res = self.client.get('/random/random_number?max=0&min=0')
        self.assertEqual(res.json()['random_number'], 0, 'El valor devuelto no es el esperado.')
