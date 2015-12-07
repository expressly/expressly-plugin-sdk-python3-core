from unittest import TestCase
from expressly import Api, api_dev_url


class PingTest(TestCase):
    def setUp(self):
        self.api = Api("api_key", api_dev_url)

    def test_request(self):
        self.assertTrue(True)
