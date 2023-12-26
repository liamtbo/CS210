'''CS lab 05: encryption and decryption broke functions
Author: Liam Bouffard
'''

import math

# done
def encrypt(msg: str) -> str:
  evens = ''
  odds = ''
  for char_index in range(0, len(msg)):
    if char_index % 2 == 0:
      evens += msg[char_index]
    else:
      odds += msg[char_index]  

  return odds + evens


# done
def decrypt(msg: str) -> str:
  msg_len = len(msg)
  
  # find middle
  if msg_len % 2 == 0: # even amount in msg_len
    middle = int(msg_len / 2)
    evens = msg[:middle]
    odds = msg[(middle):]

  else: # odd amound in msg_len
    middle = int((msg_len / 2) + 0.5)
    evens = msg[:(middle - 1)]
    odds = msg[(middle - 1):]

  decryption = ''
  odds_index = 0
  evens_index = 0
  for iter in range(msg_len):
    if iter % 2 == 0:
      decryption += odds[odds_index]
      odds_index += 1
    else:
      decryption += evens[evens_index]
      evens_index += 1

  return (decryption)


def main():
  """Main program to run our encryption/decryption process."""

  which = input('Do you wish to encrypt or decrypt a message [E/D]? ')
  if which.upper() == 'E':
    text = input('Enter a line of text to encrypt: ')
    text = str(text)
    print("Encrypted text:")
    print(encrypt(text))
  elif which.upper() == 'D':
    text = input('Enter encrypted text to decrypt: ')
    print("Decrypted text:")
    print(decrypt(text))
  else:
    raise ValueError("Invalid option, I only know E and D!")


if __name__ == '__main__':
  main()