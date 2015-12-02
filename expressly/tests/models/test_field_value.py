from unittest import TestCase
from expressly.models import FieldValue
from schematics.exceptions import ModelValidationError


class FieldValueTest(TestCase):
    def setUp(self):
        self.m = FieldValue().get_mock_object()

    def test_required(self):
        self.assertIsNotNone(self.m.field)
        self.assertIsNotNone(self.m.value)

    def test_validation(self):
        m = FieldValue()
        self.assertRaises(ModelValidationError, m.validate)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"field": "%s"' % self.m.field, json_str)
        self.assertIn('"value": "%s"' % self.m.value, json_str)
