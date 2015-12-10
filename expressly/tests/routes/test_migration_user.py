from unittest import TestCase

from expressly import routes
from expressly.tests import dummy_campaign_customer_uuid


class MigrationUserTest(TestCase):
    def setUp(self):
        self.route = routes['migration_user']

    def test_regex(self):
        self.assertRegex('/expressly/api/%s/migrate/' % dummy_campaign_customer_uuid, self.route.regex)
        self.assertRegex('/expressly/api/%s/migrate' % dummy_campaign_customer_uuid, self.route.regex)
        self.assertRegex('expressly/api/%s/migrate/' % dummy_campaign_customer_uuid, self.route.regex)
        self.assertRegex('expressly/api/%s/migrate' % dummy_campaign_customer_uuid, self.route.regex)

    def test_method(self):
        self.assertEqual('GET', self.route.method)

    def test_authorization(self):
        self.assertTrue(self.route.authorization)
