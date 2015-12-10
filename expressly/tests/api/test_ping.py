from unittest import TestCase

from schematics.validate import validate

from expressly import Api
from expressly.api_responses import PingResponse
from expressly.tests import dummy_api_key, api_dev_url


class PingTest(TestCase):
    def setUp(self):
        self.api = Api(dummy_api_key, api_dev_url, False)

    def test_request(self):
        response = self.api.ping()

        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, PingResponse)
        self.assertTrue(validate(PingResponse, response.data))

        self.assertEqual(response.data.server_status, 'Live')
        self.assertEqual(response.data.db_status, 'Live')
