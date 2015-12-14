from unittest import TestCase
from expressly.resources import CountryCodes
import random


class CountryCodesTest(TestCase):
    def setUp(self):
        self.codes = CountryCodes.codes
        self.random = random.choice(self.codes)

    def test_get_iso3(self):
        self.assertIn(self.random, self.codes)
