'''Flood-fill to count chambers in a cave.
CS 210 project.
Liam Bouffard, 10.24.2022
Credits: none
'''
import doctest
import cave
import config
import cave_view
import time

def scan_cave(cavern: list[list[str]]) -> int:
  '''Scan the cave for air pockets. Return the number of air pockets encountered.
  
  >>> cavern_1 = cave.read_cave('data//tiny-cave.txt')
  >>> scan_cave(cavern_1)
  1
  >>> cavern_2 = cave.read_cave('data//cave.txt')
  >>> scan_cave(cavern_2)
  3
  '''
  air_cuml = 0
  for row_i in range(len(cavern)):
    for col_i in range(len(cavern[0])):
      if cavern[row_i][col_i] == cave.AIR:
        air_cuml += 1
        fill(cavern, row_i, col_i)
        cave_view.change_water()
  return air_cuml

def fill(cavern: list[list[str]], row_i: int, col_i: int):
  '''Pour water into cell at row_i, col_i'''
  # fills cell with water and same color
  cavern[row_i][col_i] = cave.WATER
  cave_view.fill_cell(row_i, col_i)
  # fill up block
  row_up_i = row_i - 1
  if (row_up_i >= 0 and row_up_i < len(cavern)
      and cavern[row_up_i][col_i] == cave.AIR):
      fill(cavern, row_up_i, col_i)
  
  # fill down block
  row_down_i = row_i + 1
  if (row_down_i >= 0 and row_down_i < len(cavern)
      and cavern[row_down_i][col_i] == cave.AIR):
      fill(cavern, row_down_i, col_i)
  
  # fill left block
  col_left_i = col_i - 1
  if (col_left_i >= 0 and col_left_i < len(cavern[0])
      and cavern[row_i][col_left_i] == cave.AIR):
      fill(cavern, row_i, col_left_i)

  # fill right block
  col_right_i = col_i + 1
  if (col_right_i >= 0 and col_right_i < len(cavern[0])
      and cavern[row_i][col_right_i] == cave.AIR):
      fill(cavern, row_i, col_right_i)

def main():
  doctest.testmod()
  cavern = cave.read_cave(config.CAVE_PATH)
  cave_view.display(cavern, config.WIN_WIDTH, config.WIN_HEIGHT)
  chambers = scan_cave(cavern)
  print(f'Found {chambers} chambers')
  cave_view.prompt_to_close()


if __name__ == '__main__':
  start = time.time()
  main()
  end = time.time()
  print(end-start)