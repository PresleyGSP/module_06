"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Presley McFarlane-Goolcharan
Date: April 7th 2025
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}

class MortgageRate(Enum):
    """In this class we are storing fixed and variable mortgage rate values."""

    FIXED_5 = 0.0519
    """A fixed mortgage rate."""

    FIXED_3 = 0.0589
    """A fixed mortgage rate."""

    FIXED_1 = 0.0599
    """A fixed mortgage rate."""

    VARIABLE_5 = 0.0649
    """A variable mortgage rate."""

    VARIABLE_3 = 0.0669
    """A variable mortgage rate."""

    VARIABLE_1 = 0.0679
    """A variable mortgage rate."""

class PaymentFrequency(Enum):
    """In this class we are value for payment frequency."""

    MONTHLY = 12
    """Monthly payment frequency value."""

    BI_WEEKLY = 26
    """Bi-weekly payment frequency value."""

    WEEKLY = 52
    """Weekly payment frequency value."""