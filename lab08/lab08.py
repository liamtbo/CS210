c = 'cat'
m = 'mouse'

alist = [c, c, [c, [m], c]]

def isMouseIn(alist):
  for value in alist:
    if value == m:
      return True
    if isinstance(value, list):
      return isMouseIn(value)
  if len(alist) == 1:
    return False


print(isMouseIn(alist))