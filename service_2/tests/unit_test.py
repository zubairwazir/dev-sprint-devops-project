from flask import url_for
from flask_testing import TestCase

from service_2.app import app, alc_drink

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_alc_drink(self):

        for _ in range(20):
            response = self.client.get(url_for('get_alc_drink'))

            self.assert200(response)
            self.assertIn(response.data.decode(), alc_drink)