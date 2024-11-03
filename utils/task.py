from enum import Enum

class Task(Enum):
    MORTGAGE = "What is the payment on a 500k mortgage with a 30 year fixed rate of 6.5%?"
    INCOME_TAX = "What is the income tax on a salary of $100,000 in California?"
    PROPERTY_TAX = "What is the property tax on a $500,000 house in California?"
    CAPITAL_GAINS_TAX = "What is the capital gains tax on a $500,000 house in California?"
    SOCIAL_SECURITY_TAX = "What is the social security tax on a salary of $100,000 in California?"
    MEDICARE_TAX = "What is the medicare tax on a salary of $100,000 in California?"
    STATE_TAX = "What is the state tax on a salary of $100,000 in California?"
    FEDERAL_TAX = "What is the federal tax on a salary of $100,000 in California?"
