import re

def veri_email(email):
  pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)'
  user_input = email
  if (re.search(pattern, user_input)):
    print('valid')
  else:
    print('invalid')
  

if __name__ == '__main__':
  veri_email('lbouffa@gmail.com')