'''Jumbler: List dictionary words that match an anagram.
2022-09-37 by Liam Bouffard

Credits: me, myself, and I
'''
DICT = 'shortdict.txt'
# DICT = 'dict.txt'
dict_file = open(DICT, 'r')
 
# done
def normalize(word: str) -> list[str]:
  return sorted((word.lower()))

def find(anagram: str):
  '''
  >>> find('alpha')
  alpha

  >>> find('KAWEA')
  awake
  '''
  for line in dict_file:
    word = line.strip()
    if normalize(word) == normalize(anagram):
      print(word)


dict_file.close()



if __name__ == "__main__":
  import doctest
  doctest.testmod()
  print('doctests complete!')

'''
when alpha is doctested alone it works
when kawea is doctested alone it work
when they're doctested together the lower one fails
'''