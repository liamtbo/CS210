

a_list = ['apple', 'apple', 'banana', 'apple', 'banana']

value_dict = {}
for value in a_list:
  if value in value_dict:
    value_dict[value] += 1
  else:
    value_dict[value] = 1

print(value_dict)