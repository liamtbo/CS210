N_ROWS = 4

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

print(unpack_board('abcdefghijklmnop'))