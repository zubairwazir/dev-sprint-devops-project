from flask import url_for
from flask_testing import TestCase
import pytest, pytest_cov

from service_4.app import app, prices

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_alc_drink(self):

        for alc_drink in prices['alc_drink']:
            for soft_drink in prices['soft_drink']:

                payload = {'alc_drink': alc_drink, 'soft_drink': soft_drink}
                response = self.client.post(url_for('post_round'), json=payload)

                self.assert200(response)

                expected_price = ((prices['alc_drink'][alc_drink] + prices['soft_drink'][soft_drink]))
                self.assertEqual(response.json, expected_price)