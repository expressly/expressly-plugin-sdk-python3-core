from unittest import TestCase

from expressly.models import Invoice, Order


class InvoiceFullTest(TestCase):
    def setUp(self):
        self.m = Invoice.get_mock_object()
        self.m.orders = (
            Order.get_mock_object(),
            Order.get_mock_object()
        )

    def test_required(self):
        self.assertIsNotNone(self.m.email)
        self.assertIsNotNone(self.m.order_count)
        self.assertIsNotNone(self.m.total)
        self.assertIsNotNone(self.m.tax)

    def test_sum_total(self):
        self.assertEqual(self.m.total, sum(o.total for o in self.m.orders))
        self.assertEqual(self.m.tax, sum(o.tax for o in self.m.orders))
        self.assertEqual(self.m.post_tax_total, self.m.total + self.m.tax)

    def test_serialization(self):
        json_str = str(self.m)
        self.assertIn('"email": "%s"' % self.m.email, json_str)
        self.assertIn('"orderCount": %i' % self.m.order_count, json_str)
        self.assertIn('"orders": ', json_str)
