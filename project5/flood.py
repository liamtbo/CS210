'''FLood-fill to count chambers in a cave.
CS 210 project
Liam Bouffard, 10.24.2022
Credits: TBD
'''
import doctest



def main():
  doctest.testmod()
  cavern = cave.read_cave('data//cave.txt')
  print(cave.text(cavern))

if __name__ == '__main__':
  main()