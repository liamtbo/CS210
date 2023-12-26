'''recursion example - why does this work'''
def depth(m) -> int:
  # base cases
  if not isinstance(m, list):
    return 0
  if m == []:
    return 1
  maximum = 0
  for e in m:
    if depth(e) > maximum:
      mximum = depth(e)
  return maximum + 1

print(depth([['a', 'b'], ['x', 'y', ['z']]]))
'''
def list_depth
  for i in 
'''