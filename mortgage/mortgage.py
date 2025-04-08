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
        
        






