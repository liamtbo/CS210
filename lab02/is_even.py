import doctest
def is_even(n: int) -> bool:
  ''' determines if n is an even number.
  
  Args:
    n: an integer number
  Returns:
    True is n is an even number, False otherwise
  >>> is_even(100)
  True
  >>> is_even(101)
  False
  >>> is_even(0)
  True
  '''
  return (n % 2) == 0

def welcome():
  '''Print a welcome message.
  >>> welcome()
  Good morning, CIS 210!
  '''
  print('Good morning, CIS 210!')
  return None

def main():
  doctest.testmod()
  print(f'{is_even(2)}')
  print(f'{is_even(3)}')
  welcome()

  
if __name__ == "__main__":
  main()