from unittest import TestCase
from expressly.models import Email
from schematics.exceptions import ModelValidationError


class EmailTest(TestCase):
    def setUp(self):
        self.m = Email.get_mock_object()

    def test_required(self):
        self.assertIsNotNone(self.m.email)
        self.assertIsNotNone(self.m.alias)

    def test_validate(self):
        m = Email()
        self.assertRaises(ModelValidationError, m.validate)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"email": "%s"' % self.m.email, json_str)
        self.assertIn('"alias": "%s"' % self.m.alias, json_str)
