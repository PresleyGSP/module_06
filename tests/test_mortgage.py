"""
Description: A class used to test the Mortgage class.
Author: Presley McFarlane-Goolcharan
Date: April 7th 2025
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):

    def test_invalid_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(0, "FIXED_5", "MONTHLY", 25)

    def test_invalid_rate_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(300000, "INVALID_RATE", "MONTHLY", 25)
    
    def test_invalid_frequency_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(300000, "FIXED_5", "YEARLY", 25)
    
    def test_invalid_amortization_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(300000, "FIXED_5", "MONTHLY", 35)
    
    def test_valid_inputs_set_attributes_correctly(self):
        mortgage = Mortgage(300000, "FIXED_5", "MONTHLY", 25)
        self.assertEqual(mortgage._Mortgage__loan_amount, 300000)
        self.assertEqual(mortgage._Mortgage__rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage._Mortgage__frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage._Mortgage__amortization, 25)
    
    def test_set_loan_amount_to_negative_raises_value_error(self):
        mortgage = Mortgage(200000, "FIXED_5", "MONTHLY", 20)
        with self.assertRaises(ValueError):
            mortgage.set_loan_amount(-100000)

    def test_set_loan_amount_to_zero_raises_value_error(self):
        mortgage = Mortgage(200000, "FIXED_5", "MONTHLY", 20)
        with self.assertRaises(ValueError):
            mortgage.set_loan_amount(0)

    def test_set_loan_amount_to_positive_value_updates_amount(self):
        mortgage = Mortgage(200000, "FIXED_5", "MONTHLY", 20)
        mortgage.set_loan_amount(300000)
        self.assertEqual(mortgage.get_loan_amount(), 300000)
    
    def test_set_rate_to_valid_enum_value_updates_rate(self):
        mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 25)
        mortgage.set_rate("VARIABLE_3")
        self.assertEqual(mortgage.get_rate(), MortgageRate.VARIABLE_3)

    def test_set_rate_to_invalid_enum_value_raises_value_error(self):
        mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 25)
        with self.assertRaises(ValueError):
            mortgage.set_rate("INVALID_RATE")

    def test_set_frequency_to_valid_enum_value_updates_frequency(self):
        mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 25)
        mortgage.set_frequency("WEEKLY")
        self.assertEqual(mortgage.get_frequency(), PaymentFrequency.WEEKLY)
    
    def test_set_frequency_to_invalid_enum_value_raises_value_error(self):
        mortgage = Mortgage(250000, "FIXED_5", "MONTHLY", 25)
        with self.assertRaises(ValueError):
            mortgage.set_frequency("INVALID_FREQUENCY")