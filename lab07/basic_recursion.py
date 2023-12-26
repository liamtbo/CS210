'''
CIS 210 lab 07
Liam Bouffard

'''

import doctest

# excersize 1
def bowtie(length: int):
  '''This function used recursion to print out * in a bowtie shape
  >>> bowtie(1)
  *
  
  >>> bowtie(3)
  ***
  **
  *
  **
  ***
  '''
  # base case
  if length == 1:
    print('*')
  else:
    print('*' * length)
    bowtie(length - 1)
    print('*' * length)

# Excersize 2 
def check_vowel(letter: str) -> int:
  '''
  Returns 1 if given is a vowel, 0 otherwise
  '''
  if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
    return 1
  return 0

def count_vowels(string: str) -> int:
  '''
  counts the vowels in a string

  >>> count_vowels('Oregon')
  3

  >>> count_vowels('Hi Everyone!')
  5
  '''
  # base case
  if len(string) == 0:
    return 0

  elif check_vowel(string[0]) == 1:
    return 1 + count_vowels(string[1:])

  elif check_vowel(string[0]) == 0:
    return 0 + count_vowels(string[1:])


# Excersize 3
def is_list(var) -> bool:
  return isinstance(var, list)

def deep_reverse(a: list) -> list:
  '''
  returns the reversal of the list where any element that is a 
  list is also deep_reversed
  
  >>> deep_reverse([1, [2, 3], 4])
  [4, [3, 2], 1]

  >>> deep_reverse([1, 2, 3])
  [3, 2, 1]
  '''
  a.reverse()
  for value in a:
    if is_list(value):
      deep_reverse(value)
  return a
    

def main():
  doctest.testmod()

if __name__ == '__main__':
  main()
