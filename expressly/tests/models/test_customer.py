from datetime import date
from unittest import TestCase
from expressly.models import Customer, FieldValue, Email, Phone, Address
from schematics.exceptions import ModelValidationError


class CustomerFullTest(TestCase):
    def setUp(self):
        self.m = Customer.get_mock_object()
        self.m.gender = 'M'
        self.m.billing_address = 0
        self.m.shipping_address = 0
        self.m.company = 'Expressly'
        self.m.dob = date.today()
        self.m.online_presence = [FieldValue.get_mock_object()]
        self.m.date_updated = date.today()
        self.m.date_last_order = date.today()
        self.m.number_ordered = 1
        self.m.emails = [Email.get_mock_object()]
        self.m.phones = [Phone.get_mock_object()]
        self.m.addresses = [Address.get_mock_object()]

    def test_required(self):
        self.assertIsNotNone(self.m.first_name)
        self.assertIsNotNone(self.m.last_name)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"firstName": "%s"' % self.m.first_name, json_str)
        self.assertIn('"lastName": "%s"' % self.m.last_name, json_str)
        self.assertIn('"gender": "%s"' % self.m.gender, json_str)
        self.assertIn('"billingAddress": %u' % self.m.billing_address, json_str)
        self.assertIn('"shippingAddress": %u' % self.m.shipping_address, json_str)
        self.assertIn('"company": "%s"' % self.m.company, json_str)
        self.assertIn('"dob": "%s"' % self.m.dob, json_str)
        # self.assertIn('"onlinePresence": %s' % self.m.online_presence, json_str)
        self.assertIn('"dateUpdated": "%s"' % self.m.date_updated, json_str)
        self.assertIn('"dateLastOrder": "%s"' % self.m.date_last_order, json_str)
        self.assertIn('"numberOrdered": %u' % self.m.number_ordered, json_str)
        # self.assertIn('"emails": %s' % self.m.emails, json_str)
        # self.assertIn('"phones": %s' % self.m.phones, json_str)
        # self.assertIn('"addresses": %s' % self.m.addresses, json_str)

    class CustomerPartialTest(TestCase):
        def setUp(self):
            self.m = Customer.get_mock_object()

        def test_required(self):
            self.assertIsNotNone(self.m.first_name)
            self.assertIsNotNone(self.m.last_name)

        def test_serialization(self):
            json_str = str(self.m)
            self.assertIn('"firstName": "%s"' % self.m.first_name, json_str)
            self.assertIn('"lastName": "%s"' % self.m.last_name, json_str)

    class CustomerMissingTest(TestCase):
        def setUp(self):
            self.m = Customer()

        def test_validation(self):
            self.assertRaises(ModelValidationError, self.m.validate)

        def test_serialization(self):
            json_str = str(self.m)
            self.assertIsNone(self.m.gender)
            self.assertNotIn('gender', json_str)

            self.assertIsNone(self.m.billing_address)
            self.assertNotIn('billingAddress', json_str)

            self.assertIsNone(self.m.shipping_address)
            self.assertNotIn('shippingAddress', json_str)

            self.assertIsNone(self.m.company)
            self.assertNotIn('company', json_str)

            self.assertIsNone(self.m.dob)
            self.assertNotIn('dob', json_str)

            self.assertIsNone(self.m.online_presence)
            self.assertNotIn('onlinePresence', json_str)

            self.assertIsNone(self.m.date_updated)
            self.assertNotIn('dateUpdated', json_str)

            self.assertIsNone(self.m.date_last_order)
            self.assertNotIn('dateLastOrder', json_str)

            self.assertIsNone(self.m.number_ordered)
            self.assertNotIn('numberOrdered', json_str)

            self.assertIsNone(self.m.emails)
            self.assertNotIn('emails', json_str)

            self.assertIsNone(self.m.phones)
            self.assertNotIn('phones', json_str)

            self.assertIsNone(self.m.addresses)
            self.assertNotIn('addresses', json_str)
