"""Boggler:  Boggle game solver. CS 210, Fall 2022.
Sample solution by Michal Young.
Credits: TBD
"""
import doctest
import sys

import board_view
import config

# Possible search outcomes
NOPE = "Nope"       # Not a match, nor a prefix of a match
MATCH = "Match"     # Exact match to a valid word
PREFIX = "Prefix"   # Not an exact match, but a prefix (keep searching!)

# Special character in position that is
# already in use
IN_USE = "@"

# Max word length is 16, so we can just list all
# the point values.
#
#         0  1  2  3  4  5  6  7  8
POINTS = [0, 0, 0, 1, 1, 2, 3, 5, 11,
          11, 11, 11, 11, 11, 11, 11, 11 ]
#          9  10  11  12  13  14  15  16


def test_it():
    """A little extra work to keep text display from
    interfering with doctests.
    """
    saved_flag = config.TEXT_VIEW
    config.TEXT_VIEW = False
    doctest.testmod(verbose=True)
    config.TEXT_VIEW = saved_flag

def read_dict(path: str) -> list[str]:
    """Returns ordered list of valid, normalized words from dictionary.

    >>> read_dict("data/shortdict.txt")
    ['ALPHA', 'BED', 'BETA', 'DELTA', 'GAMMA', 'OMEGA']
    """
    words = []
    with open(path) as dict_file:
        for line in dict_file:
            word = line.strip()
            if allowed(word):
                words.append(normalize(word))
    return sorted(words)

def allowed(s: str) -> bool:
    """Is s a legal Boggle word?

    >>> allowed("am")  ## Too short
    False

    >>> allowed("de novo")  ## Non-alphabetic
    False

    >>> allowed("about-face")  ## Non-alphabetic
    False
    """
    return (len(s) >= 3 and s.isalpha())


def normalize(s: str) -> str:
    """Canonical for strings in dictionary or on board
    >>> normalize("filter")
    'FILTER'
    """
    return s.upper()

def search(candidate: str, word_list: list[str]) -> str:
    """Determine whether candidate is a MATCH, a PREFIX of a match, or a big NOPE
    Note word list MUST be in sorted order.

    >>> search("ALPHA", ['ALPHA', 'BETA', 'GAMMA']) == MATCH
    True

    >>> search("BE", ['ALPHA', 'BETA', 'GAMMA']) == PREFIX
    True

    >>> search("FOX", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
    True

    >>> search("ZZZZ", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
    True
    """
    low = 0
    high = len(word_list) - 1
    while low <= high:
        mid = (low + high) // 2
        check = word_list[mid]
        if check == candidate:
            return MATCH
        if check < candidate:
            low = mid + 1
        if check > candidate:
            high = mid - 1
    if low < len(word_list) and word_list[low].startswith(candidate):
        return PREFIX
    return NOPE

def get_board_letters() -> str:
    """Get a valid string to form a Boggle board
    from the user.  May produce diagnostic
    output and quit.
    """
    while True:
        board_string = input("Boggle board letters (or 'return' to exit)> ")
        if allowed(board_string) and len(board_string) == config.BOARD_SIZE:
            return board_string
        elif len(board_string) == 0:
            print(f"OK, sorry it didn't work out")
            sys.exit(0)
        else:
            print(f'"{board_string}" is not a valid Boggle board')
            print(f'Please enter exactly {config.BOARD_SIZE} letters (or empty to quit)')
    return normalize(board_string)


def unpack_board(letters: str, rows=config.N_ROWS) -> list[list[str]]:
    """Unpack a single string of characters into
    a square matrix of individual characters, N_ROWS x N_ROWS.

    >>> unpack_board("abcdefghi", rows=3)
    [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

    >>> unpack_board("abcdefghijklmnop", rows=4)
    [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
    """
    board = []
    idx = 0  # Next letter
    for row_i in range(rows):
        row = []
        for col_i in range(rows):
            row.append(letters[idx])
            idx += 1
        board.append(row)
    return board

def boggle_solve(board: list[list[str]], words: list[str]) -> list[str]:
    """Find all the words that can be made by traversing
    the boggle board in all 8 directions.  Returns sorted list without
    duplicates.

    >>> board = unpack_board("PLXXMEXXXAXXSXXX", rows=4)
    >>> words = read_dict("data/dict.txt")
    >>> boggle_solve(board, words)
    ['AMP', 'AMPLE', 'AXE', 'AXLE', 'ELM', 'EXAM', 'LEA', 'MAX', 'PEA', 'PLEA', 'SAME', 'SAMPLE', 'SAX']
    """
    solutions = []

    def solve(row: int, col: int, prefix: str):
        """One solution step"""
        if row < 0 or row >= config.N_ROWS:
            return
        if col < 0 or col >= config.N_COLS:
            return
        letter = board[row][col]
        prefix = prefix + letter
        status = search(prefix, words)
        if status == NOPE:
            return

        board[row][col] = IN_USE  # Prevent reusing
        board_view.mark_occupied(row, col)

        ## further exploration goes here
        if status == MATCH:
            solutions.append(prefix)
            board_view.celebrate(prefix)

        if status == MATCH or status == PREFIX:
            # Keep searching - checks all surrounding letters 
            for d_row in [0, -1, 1]:
                for d_col in [0, -1, 1]:
                    solve(row+d_row, col+d_col, prefix)

        # Restore
        board[row][col] = letter
        board_view.mark_unoccupied(row, col)

    # Look for solutions starting from each board position
    for row_i in range(config.N_ROWS):
        for col_i in range(config.N_COLS):
            solve(row_i, col_i, "")

    # Return solutions without duplicates, in sorted order
    solutions = list(set(solutions))
    return sorted(solutions)

def score(solutions: list[str]) -> int:
    """Sum of scores for each solution

    >>> score(["ALPHA", "BETA", "ABSENTMINDED"])
    14
    """
    total = 0
    for word in solutions:
        total += POINTS[len(word)]
    return total


def main():
    # gets sorted list of word from path
    words = read_dict(config.DICT_PATH)
    # holds boggler letters
    board_string = get_board_letters()
    # reduntant?, get board_letters already normalizes them
    board_string = normalize(board_string)
    # makes a grid out of board_string, n x n
    board = unpack_board(board_string)
    # graphics
    board_view.display(board)
    # finds all combination of 
    solutions = boggle_solve(board, words)
    print(solutions)
    earned = score(solutions)
    print(f"{score(solutions)} points")
    board_view.prompt_to_close()

if __name__ == "__main__":
    # test_it()
    main()
