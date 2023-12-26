'''Boggler: Boggle game solver. CS 210, Fall 2022.
Liam Bouffard
Credits: TBD
'''
import doctest
import config

# List of words to search for
DICT_PATH = 'data/shortdict.txt'

# Boggle rules
MIN_WORD = 3 # A word must be at least 3 chracters to count
# Possible search outcomes
NOPE = 'Nope' # not a math, nor a prefix of a match
MATCH = 'Match' # exact match to a valid word
PREFIX = 'Prefix' # not an exact match, but a prefix (keep searching)


def normalize(s: str) -> str:
  '''Canonical for strings in dictionary or on board
  >>> normalize('filter')
  'FILTER'
  '''
  return s.upper()

def allowed(s: str) -> bool:
  '''Is s a legal Boggle word?
  >>> allowed('am') ## Too short
  False
  
  >>> allowed('de novo')
  False
  
  >>> allowed('about-face')
  False
  '''
  if (len(s) >= MIN_WORD) and (s.isalpha()):
    return True
  else:
    return False

def read_dict(path:str) -> list[str]:
  '''Returns ordered list of valid, normalized words from dictionary.
  
  >>> read_dict('data/shortdict.txt')
  ['ALPHA', 'BETA', 'DELTA', 'GAMMA', 'OMEGA']
  '''
  word_list = []
  with open(path) as wordfile:
    for word in wordfile:
      word = normalize(word.strip())
      if allowed(word):
        word_list.append(word)
  word_list = sorted(word_list)

  return word_list

read_dict('data/shortdict.txt')



def search(candidate: str, word_list: list[str]) -> str:
  '''Determine whether candidate is a MATCH, a Prefix of a match, or a big NOPE
  Note word list must be in sorted order.
  
  >>> search('ALPHA', ['ALPHA', 'BETA', 'GAMMA']) == MATCH
  True

  >>> search('BE', ['ALPHA', 'BETA', 'GAMMA']) == PREFIX
  True

  >>> search("FOX", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
  True

  >>> search("ZZZZ", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
  True
  '''
  low = 0
  high = len(word_list) - 1
  while low <= high:
    mid = (high + low) // 2
    if candidate == word_list[mid]:
      return MATCH
    elif candidate < word_list[mid]:
      high = mid - 1
    elif candidate > word_list[mid]:
      low = mid + 1
    if (low < len(word_list) - 1) and word_list[mid].startswith(candidate):
      return PREFIX

  return NOPE
  
search("FOX", ['ALPHA', 'BETA', 'GAMMA'])

def main():
    words = read_dict(config.DICT_PATH)
    board_string = get_board_letters()
    board_string = normalize(board_string)
    board = unpack_board(board_string)
    board_view.display(board)
    solutions = boggle_solve(board, words)
    print(solutions)
    earned = score(solutions)
    print(f"{score(solutions)} points")
    board_view.prompt_to_close()

if __name__ == '__main__':
  doctest.testmod()
  print('Doctests complete')
  main()