from data_fetch.twitter.NumberParser import NumberParser
import unittest


class TestNumberParser(unittest.TestCase):

    def test_int_with_space(self):
        num_str = "123 456"
        self.assertEqual(NumberParser.int_with_space(num_str), 123456)

    def test_int_with_modifier_thousand(self):
        num_str = "25 tys."
        self.assertEqual(NumberParser.int_with_modifier(num_str), 25000)

    def test_int_with_modifier_million(self):
        num_str = "16,5 mln."
        self.assertEqual(NumberParser.int_with_modifier(num_str), 16_500_000)
