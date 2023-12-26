
aTuple = ('+', ('-', 7, 3), 5)
def cumulative(atuple):
  cuml = 0
  if aTuple[0] == '+':
    for value in aTuple:
      if isinstance(value, tuple):
        return cumulative(value)
      if isinstance(value, int):
        cuml += value
  if aTuple[0] == '-':
    for value in aTuple:
      