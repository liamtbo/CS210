'''Jumbler: List dictionary words that match an anagram.
2022-09-37 by Liam Bouffard

Credits: Michal Young
'''
# DICT = 'shortdict.txt'
DICT = 'dict.txt'
 
# done
def normalize(word: str) -> list[str]:
  '''Returns a list of characters that is canonical for anagrams.
  >>> normalize('gamma') == normalize('magam')
  True

  >>> normalize('MAGAM') == normalize('gamma')
  True

  >>> normalize('KAWEA') == normalize('awake')
  True

  >>> normalize('KAWEA') == normalize('gamma')
  False
  '''  
  return sorted((word.lower()).replace(' ', ''))

def find(anagram: str):
  ''' loops throught the dict_file to find a word with a matching noralization
  >>> find('AgEmo')
  omega

  >>> find('nosuchword')

  >>> find('alpha')
  alpha

  >>> find('KAWEA')
  awake
  '''
  dict_file = open(DICT, 'r')
  normAna = normalize(anagram)
  for line in dict_file:
    word = line.strip()
    if normalize(word) == normAna:
      print(word)
  
  dict_file.close()

def main():
  anagram = input('Anagram to find> ')
  find(anagram)

if __name__ == "__main__":
  main()
  # import doctest
  # doctest.testmod()
  # print('doctests complete!')