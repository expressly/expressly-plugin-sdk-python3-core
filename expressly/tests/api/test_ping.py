from unittest import TestCase

from expressly import Api
from expressly.tests import dummy_api_key, api_dev_url


class PingTest(TestCase):
    def setUp(self):
        self.api = Api(dummy_api_key, api_dev_url, False)

    def test_request(self):
        response = self.api.ping()

        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data']['Server'], 'Live')
        self.assertEqual(response['data']['DB Status'], 'Live')
