from datetime import datetime
from unittest import TestCase

from decimal import Decimal

from expressly.models import Order


class OrderFullTest(TestCase):
    def setUp(self):
        date_time = datetime.utcnow().isoformat('T')

        self.m = Order.get_mock_object()
        self.m.date = date_time
        self.m.tax = Decimal(self.m.tax).quantize(Decimal('.01'))
        self.m.total = Decimal(self.m.total).quantize(Decimal('.01'))

    def test_required(self):
        self.assertIsNotNone(self.m.date)
        self.assertIsNotNone(self.m.item_count)
        self.assertIsNotNone(self.m.total)
        self.assertIsNotNone(self.m.tax)
        self.assertIsNotNone(self.m.post_tax_total)

    def test_validate(self):
        self.assertIsNone(self.m.validate())

    def test_total_addition(self):
        self.assertEqual(self.m.total + self.m.tax, self.m.post_tax_total)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"date": "%s"' % self.m.date, json_str)
        self.assertIn('"itemCount": %i' % self.m.item_count, json_str)
        self.assertIn('"preTaxTotal": ', json_str)
        self.assertIn('"tax": ', json_str)
        self.assertIn('"postTaxTotal": ', json_str)
