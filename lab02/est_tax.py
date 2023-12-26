'''est_tax: calculcates ones estimated tax
2022-10-06 by Liam Bouffard

Credits: None
'''
import doctest

def est_tax(income: float, exemptions: float) -> float:
  '''Generates an estimate for federal income tax and print the result. Assumes a simple standard deduction of $12500 and a flat tax rate of 20%.
  
    Args:
      income: the income, for which the tax is being computed
      exemptions: the number of exemptions claimed by the tax payer

    Returns:
      The tax owed for the provided income and number of exceptions.

    >>> est_tax(43_000, 1)
    Estimated tax is: 3580.0
    3580.0
  '''
  # Constants for the standard exemption and deduction (USD)
  STD_DEDUCT = 12550
  STD_EXEMPT = 12550

  # Constant for the flat tax rate of 20%
  TAX_RATE = .20

  # Calculate federal tax by adjusting reported income and applying tax rate
  taxable_income = taxable(income, exemptions, STD_EXEMPT, STD_DEDUCT)
  estimated_tax = taxable_income * TAX_RATE

  print('Estimated tax is:', estimated_tax)

  return estimated_tax

def taxable(income: float, exemptions: int, exempt_amount: float, deduct_amount: float):
  '''Adjust gross income to taxable income by applying the standard deduction and exemptions.
  
  Args:
    income: gross income, for which the tax is being computed
    exemptions: the number of personal exemptions
    exempt_amount: the dollar amount for each exemption
    deduct_amount: the dollar amount for the standard deduction

  Returns:
    TODO: Should this function return a value or print the result??
  
  >>> taxable(43_000, 1, 12_550, 12_550)
  17900
  '''
  taxable_income = income - deduct_amount
  exempt_adjust = exempt_amount * exemptions
  taxable_income = taxable_income - exempt_adjust

  return taxable_income

def main():
  doctest.testmod()

if __name__ == '__main__':
  main()