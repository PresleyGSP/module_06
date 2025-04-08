"""
Description: A class meant to manage Mortgage options.
Author: Presley McFarlane-Goolcharan
Date: April 7th 2025
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


class Mortgage:
    """This class will make use of mortgage rates, payment frequency values and amortization."""

    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: int):
        # Validate Loan Amount
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        #Validating Rate
        try:
                self.__rate = MortgageRate[rate]
        except Exception as e:
                raise ValueError("Rate provided is invalid.")
        
        # Validate Frequency
        try:
                self.__frequency = PaymentFrequency[frequency]
        except Exception as e:
                raise ValueError("Frequency provided is invalid.")
        
        # Validate Amortization
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization

    def get_loan_amount(self):
        """Returns the mortgage loan amount."""

        return self.__loan_amount
    
    def set_loan_amount(self, amount):
          """Sets a new mortgage loan amount.
          
          Raises:
                ValueError: If the amount is zero or negative.
        
          """
          if amount <= 0:
                raise ValueError("Loan Amount must be positive.")
          self.__loan_amount = amount
    
    def get_rate(self):
          """Returns the mortgage interest rate."""

          return self.__rate
    
    def set_rate(self, rate):
          """
          Sets the mortgage interest rate enum value.
          
          Args:
            rate (str): The string key of a MortgageRate enum number.

          Raises:
                ValueError: If the provided rate is invalid.
          """
          try:
                self.__rate = MortgageRate[rate]
          except Exception as e:
                raise ValueError("Rate provided is invalid.")
    
    def get_frequency(self):
          """Returns the payment frequency value."""

          return self.__frequency
    
    def set_frequency(self, frequency):
          """
          Sets the mortgage payment frequency.

          Args:
                frequency (str): The string key of a PaymentFrequency enum member.
          
          Raises:
                ValueError: If the frequency is not valid.
          """
          try:
                self.__frequency = PaymentFrequency[frequency]
          except Exception as e:
                raise ValueError("Frequency provided is invalid.")
    
    def get_amortization(self):
        """Returns the amortization period in years."""

        return self.__amortization
    
    def set_amortization(self, amortization):
          """
          Sets the amortization period.

          Args:
                amortization (int): The number of years to repay the mortgage.
          Raises:
                ValueError: If the amortization is not in the list of valid options
          """

          if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
          self.__amortization = amortization
                





