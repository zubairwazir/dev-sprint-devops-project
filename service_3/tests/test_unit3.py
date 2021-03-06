from flask import url_for
from flask_testing import TestCase

from service_3.app import app, soft_drink
import pytest, pytest_cov

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_soft_drink(self):
        for _ in range(20):
            response = self.client.get(url_for('get_soft_drink'))

            self.assert200(response)
            self.assertIn(response.data.decode(), soft_drink)