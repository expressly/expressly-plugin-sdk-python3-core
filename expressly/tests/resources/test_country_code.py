from unittest import TestCase
from expressly.resources import CountryCodes
import random


class CountryCodesTest(TestCase):
    def setUp(self):
        self.codes = CountryCodes()
        self.random = random.choice(self.codes.codes)

    def test_get_iso2(self):
        self.assertEqual(self.random.iso2, self.codes.iso2(self.random.iso2))
        self.assertEqual(self.random.iso2, self.codes.iso2(self.random.iso3))

    def test_get_iso2_invalid(self):
        self.assertIsNone(self.codes.iso2('123'))

    def test_get_iso2_all(self):
        self.assertEqual(len(self.codes.codes), len(self.codes.iso2()))

    def test_get_iso3(self):
        self.assertEqual(self.random.iso3, self.codes.iso3(self.random.iso2))
        self.assertEqual(self.random.iso3, self.codes.iso3(self.random.iso3))

    def test_get_iso3_invalid(self):
        self.assertIsNone(self.codes.iso3('123'))

    def test_get_iso3_all(self):
        self.assertEqual(len(self.codes.codes), len(self.codes.iso3()))
