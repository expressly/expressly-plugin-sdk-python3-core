from unittest import TestCase

from httpretty import activate, register_uri, POST

from expressly import Api
from expressly.tests import api_dev_url, dummy_api_key, dummy_campaign_customer_uuid


class CustomerMigrationSuccessTest(TestCase):
    def setUp(self):
        self.api = Api(dummy_api_key, api_dev_url, False)

    @activate
    def test_migration_status_migrated(self):
        register_uri(
            POST,
            'http://%s/api/v2/migration/%s/success' % (api_dev_url, dummy_campaign_customer_uuid),
            body=b'{"success":true,"msg":"User registered as migrated"}',
            status=200,
            content_type='application/json'
        )

        response = self.api.customer_migration_status(dummy_campaign_customer_uuid)

        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data']['success'], True)
        self.assertEqual(response['data']['msg'], 'User registered as migrated')

    @activate
    def test_migration_status_exists(self):
        register_uri(
            POST,
            'http://%s/api/v2/migration/%s/success' % (api_dev_url, dummy_campaign_customer_uuid),
            body=b'{"success":true,"msg":"User already migrated"}',
            status=200,
            content_type='application/json'
        )

        response = self.api.customer_migration_status(dummy_campaign_customer_uuid)

        self.assertEqual(response['status'], 200)
        self.assertEqual(response['data']['success'], True)
        self.assertEqual(response['data']['msg'], 'User already migrated')
