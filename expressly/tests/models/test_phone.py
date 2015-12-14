from unittest import TestCase
from expressly.models import Phone
from schematics.exceptions import ModelValidationError


class PhoneTest(TestCase):
    def setUp(self):
        self.m = Phone.get_mock_object()

    def test_required(self):
        self.assertIsNotNone(self.m.type)
        self.assertIsNotNone(self.m.number)
        self.assertIsNotNone(self.m.country_code)

    def test_validate(self):
        m = Phone()
        m.country_code = '123'

        self.assertRaises(ModelValidationError, m.validate)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"type": "%s"' % self.m.type, json_str)
        self.assertIn('"number": "%s"' % self.m.number, json_str)
        self.assertIn('"countryCode": "%s"' % self.m.country_code, json_str)
