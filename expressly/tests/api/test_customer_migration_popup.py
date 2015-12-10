from unittest import TestCase
from httpretty import GET, activate, register_uri
from expressly import Api
from expressly.errors import InvalidHTMLError
from expressly.tests import api_dev_url, dummy_api_key, dummy_campaign_customer_uuid


class CustomerMigrationPopupTest(TestCase):
    def setUp(self):
        self.api = Api(dummy_api_key, api_dev_url, False)

    @activate
    def test_migration_popup(self):
        register_uri(
            GET,
            'http://%s/api/v2/migration/%s' % (api_dev_url, dummy_campaign_customer_uuid),
            body=b'<div></div>',
            status=200,
            content_type='text/html'
        )

        try:
            response = self.api.get_migration_popup(dummy_campaign_customer_uuid)

            self.assertTrue(response.status, 200)
            self.assertEqual(response.data, '<div></div>')
        except InvalidHTMLError:
            self.fail("Passed HTML was not valid.")
