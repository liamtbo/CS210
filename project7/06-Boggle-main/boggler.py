'''Boggler: Boggle game solver. CS 210, Fall 2022.
Liam Bouffard
Credits: None
'''
import doctest
import config
import  sys
import math
import board_view

# List of words to search for
DICT_PATH = 'data/shortdict.txt'

# Boggle rules
MIN_WORD = 3 # A word must be at least 3 chracters to count
# Possible search outcomes
NOPE = 'Nope' # not a math, nor a prefix of a match
MATCH = 'Match' # exact match to a valid word
PREFIX = 'Prefix' # not an exact match, but a prefix (keep searching)
# Board dimensions
N_ROWS = 4
N_COLS = N_ROWS
BOARD_SIZE = N_ROWS * N_COLS
# Special character in position that is
# already in use
IN_USE = '@'

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

def normalize(s: str) -> str:
  '''Canonical for strings in dictionary or on board
  >>> normalize('filter')
  'FILTER'
  '''
  return s.upper()

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
  if (low < len(word_list) - 1) and word_list[low].startswith(candidate):
    return PREFIX
  else:
    return NOPE

def get_board_letters() -> str:
  '''Get a valid string to form a boggle board 
  from the user. My produce diagnostic output and qut'''
  while True:
    board_string = input("Boggle board letters (or 'return' to exit)> ")
    if allowed(board_string) and len(board_string) == BOARD_SIZE:
      return board_string
    elif len(board_string) == 0:
      print(f"OK, sorry it didn't workout")
      sys.exit(0)
    else:
      print(f'"{board_string}" is not a valid Boggle board')
      print(f'Please enter exactly 16 letters (or empty to quit)')

def unpack_board(letters: str) -> list[list[str]]:
  '''Unpack a single string of characters into
  a matrix of individual characters, N_ROWS x N_COLS
  
  >>> unpack_board('abcdefghijklmnop')
  [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
  '''
  board_list = []
  right_slice = N_ROWS
  left_slice = 0
  for row in range(int(N_ROWS)):
    board_list.append(list(letters[left_slice:right_slice]))
    left_slice += N_ROWS
    right_slice += N_ROWS
  return board_list

def boggle_solve(board: list[list[str]], words: list[str]) -> list[str]:
  '''Find all the words that can be made by traversing
  the boggle board in all 8 diretions. Returns sorted list without duplicates
  
  >>> board = unpack_board('PLXXMEXXXAXXSXXX')
  >>> words = read_dict('data/dict.txt')
  >>> boggle_solve(board, words)
  ['AMP', 'AMPLE', 'AXE', 'AXLE', 'ELM', 'EXAM', 'LEA', 'MAX', 'PEA', 'PLEA', 'SAME', 'SAMPLE', 'SAX']
  '''
  solutions = []
  
  def solve(row: int, col: int, prefix: str):
    '''One solution step'''
    if -5 < row < N_ROWS and -5 < col < N_COLS:
      # checks if letter is always in use
      if board[row][col] != IN_USE:
        letter = board[row][col]
        prefix += letter
        status = search(prefix, words)
        if status == NOPE:
          return
        if status == MATCH:
          solutions.append(prefix)
        if status == MATCH or status == PREFIX:
          # Keep searching
          board[row][col] = IN_USE
          board_view.mark_occupied(row, col)
          # *** Recursive calls go here ***
          for d_row in [0, -1, 1]:
            for d_col in [0, -1, 1]:
              solve(row+d_row, col+d_col, prefix)
          # Restore letter for further search
          board[row][col] = letter
          board_view.mark_unoccupied(row, col)
    else:
      return

  # look for solutions starting from each board
  for row in range(N_ROWS):
    for col in range(N_COLS):
      solve(row, col, '')

  # return solutions without duplicates, in sorted order
  solutions = list(set(solutions))
  return sorted(solutions)

POINTS = [0, 0, 0, 1, 1, 2, 3, 5, 11,
        11, 11, 11, 11, 11, 11, 11, 11]

def word_score(word: str) -> int:
  '''Standard point value in Boggle'''
  assert len(word) <= 16
  return POINTS[len(word)]

def score(solutions: list[str]) -> int:
  '''sum of scores for each solution
  
  >>> score(['ALPHA', 'BETA', 'ABSENTMINDED'])
  14
  '''
  point_cuml = 0
  for word in solutions:
    point_cuml += word_score(word)
  return point_cuml


def main():
  words = read_dict(config.DICT_PATH)
  board_string = get_board_letters()
  board_string = normalize(board_string)
  board = unpack_board(board_string)
  board_view.display(board)
  solutions = boggle_solve(board, words)
  print(solutions)
  print(f'{score(solutions)} points')
  board_view.prompt_to_close()

if __name__ == '__main__':
  doctest.testmod()
  print('Doctests complete')
  main()