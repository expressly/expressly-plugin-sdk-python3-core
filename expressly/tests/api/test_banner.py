from unittest import TestCase

from httpretty import activate, register_uri, GET
from schematics.validate import validate

from expressly import Api
from expressly.api_responses import BannerResponse
from expressly.tests import dummy_api_key, api_dev_url, dummy_campaign_uuid


class BannerTest(TestCase):
    def setUp(self):
        self.api = Api(dummy_api_key, api_dev_url, False)
        self.dummy_email = 'test@test.com'

    @activate
    def test_request(self):
        register_uri(
            GET,
            'http://%s/api/v2/banner/%s?email=%s' % (api_dev_url, dummy_campaign_uuid, self.dummy_email),
            body=bytearray("""
            {
                "bannerImageUrl": "https://buyexpressly.com/assets/banner/awesome-banner.jpg",
                "migrationLink": "https://www.myblog.com/expressly/api/3aff1880-b0f5-45bd-8f33-247f55981f2c"
            }""", 'utf-8'),
            status=200,
            content_type='application/json'
        )

        response = self.api.get_banner(dummy_campaign_uuid, self.dummy_email)

        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, BannerResponse)
        self.assertTrue(validate(BannerResponse, response.data))
