from unittest import TestCase
from expressly import Api
from expressly.tests import dummy_api_key, api_dev_url


class RegisterTest(TestCase):
    def setUp(self):
        self.api = Api(dummy_api_key, api_dev_url, False)

    def test_request(self):
        self.assertTrue(True)
