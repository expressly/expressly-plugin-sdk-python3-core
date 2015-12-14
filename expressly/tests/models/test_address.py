from unittest import TestCase
from expressly.models import Address
from expressly.resources import CountryCodes
from schematics.exceptions import ModelValidationError


class AddressFullTest(TestCase):
    def setUp(self):
        self.m = Address.get_mock_object()
        self.m.address2 = 'Address 2'
        self.m.city = 'London'
        self.m.company_name = 'Expressly'
        self.m.zip = 'W2 6LG'
        self.m.phone = 0
        self.m.state = 'London'

    def test_required(self):
        self.assertIsNotNone(self.m.first_name)
        self.assertIsNotNone(self.m.last_name)
        self.assertIsNotNone(self.m.address1)
        self.assertIsNotNone(self.m.alias)
        self.assertIsNotNone(self.m.country)

    def test_optional(self):
        self.assertIsNotNone(self.m.address2)
        self.assertIsNotNone(self.m.city)
        self.assertIsNotNone(self.m.company_name)
        self.assertIsNotNone(self.m.zip)
        self.assertIsNotNone(self.m.phone)
        self.assertIsNotNone(self.m.state)

    def test_country_code_valid(self):
        self.assertIn(self.m.country, CountryCodes.codes)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"firstName": "%s"' % self.m.first_name, json_str)
        self.assertIn('"lastName": "%s"' % self.m.last_name, json_str)
        self.assertIn('"address1": "%s"' % self.m.address1, json_str)
        self.assertIn('"address2": "%s"' % self.m.address2, json_str)
        self.assertIn('"city": "%s"' % self.m.city, json_str)
        self.assertIn('"companyName": "%s"' % self.m.company_name, json_str)
        self.assertIn('"zip": "%s"' % self.m.zip, json_str)
        self.assertIn('"phone": %u' % self.m.phone, json_str)
        self.assertIn('"alias": "%s"' % self.m.alias, json_str)
        self.assertIn('"stateProvince": "%s"' % self.m.state, json_str)
        self.assertIn('"country": "%s"' % self.m.country, json_str)


class AddressPartialTest(TestCase):
    def setUp(self):
        self.m = Address.get_mock_object()

    def test_required(self):
        self.assertIsNotNone(self.m.first_name)
        self.assertIsNotNone(self.m.last_name)
        self.assertIsNotNone(self.m.address1)
        self.assertIsNotNone(self.m.alias)
        self.assertIsNotNone(self.m.country)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"firstName": "%s"' % self.m.first_name, json_str)
        self.assertIn('"lastName": "%s"' % self.m.last_name, json_str)
        self.assertIn('"address1": "%s"' % self.m.address1, json_str)
        self.assertIn('"alias": "%s"' % self.m.alias, json_str)
        self.assertIn('"country": "%s"' % self.m.country, json_str)


class AddressMissingTest(TestCase):
    def setUp(self):
        self.m = Address()

    def test_validation(self):
        self.assertRaises(ModelValidationError, self.m.validate)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIsNone(self.m.address2)
        self.assertNotIn('address2', json_str)

        self.assertIsNone(self.m.city)
        self.assertNotIn('city', json_str)

        self.assertIsNone(self.m.zip)
        self.assertNotIn('zip', json_str)

        self.assertIsNone(self.m.phone)
        self.assertNotIn('phone', json_str)

        self.assertIsNone(self.m.state)
        self.assertNotIn('state', json_str)
