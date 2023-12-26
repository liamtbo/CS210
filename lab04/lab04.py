'''lab04 Oct 19, 2022
creator: Liam Bouffard
'''

def hello(firstname: str):
  '''TODO: Write a one-line docstring!'''
  print('Hello, '+firstname+'!')
  return None

def ciao(firstname: str):
  '''TODO: Write a one-line doctring!'''
  print('Ciao, '+firstname+'!')
  return None

def greeting(f, s: str) -> None:
  '''calls function passed as argument'''
  if f == hello:
    print('Calling hello:')
    hello(s)
  elif f == ciao:
    print('Calling ciao:')
    ciao(s)
  return None

