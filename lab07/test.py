

def reverse_it(alist: list) -> list:
  if alist:
    return reverse_it(alist[1:]) + alist[:1]
  else:
    return []


print(reverse_it([1, 2, 3, 4, 5, 6]))