'''Enrollment analysis: Summary reports of majors enrolled in a class
CS 210 project, Fall 2022
Author: Liam Bouffard
Credits: TBD
'''

import doctest
import csv

# done
def read_csv_column(path: str, field: str) -> list[str]:
  '''read one column from a CSV file with headers into a list of strings.
  >>> read_csv_column('data//test_roster.csv', 'Major')
  ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
  '''
  with open(path) as csv_file:
    reader = csv.DictReader(csv_file)

    # initializing vars
    column_dict = {}
    column_key = str(field)
    column_dict[column_key] = []

    # looping over rows, then looping over each key in the row, if key == field, then append the value to the list
    for row in reader:
      for key in row:
        if key == field:
          column_dict[column_key].append(row[key])

  return column_dict[column_key]

# done
def counts(column: list[str]) -> dict[str, int]:
  '''Returns a dict with counts of elements in column.
  
  >>> counts(['dog', 'cat', 'cat', 'rabbit', 'dog'])
  {'dog': 2, 'cat': 2, 'rabbit': 1}
  '''
  value_dict = {}
  for value in column:
    if value in value_dict:
      value_dict[value] += 1
    else:
      value_dict[value] = 1

  return(value_dict)

def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
  '''read a CSV witha  column headers into a dict with selected key and value fields.
  
  >>> read_csv_dict('data//test_programs.csv', key_field='Code', value_field='Program Name')
  {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
  '''
  with open(path) as csv_file:
    reader = csv.DictReader(csv_file)
    key_value_dict = {}
    for row in reader:
      key = row[key_field]
      value = row[value_field]
      key_value_dict[key] = value
  
  return key_value_dict

def items_v_k(counts: dict[str, int]) -> list[tuple]:
  '''takes a key and correponsing value, reverses the pair, and appends it to a list as a tuple
  >>> items_v_k({'walrus': 8, 'panda': 10, 'churro': 40})
  [(8, 'walrus'), (10, 'panda'), (40, 'churro')]
  '''
  by_count = []
  for code,  count in counts.items():
    pair = (count, code)
    by_count.append(pair)
  return by_count

def main():
  doctest.testmod()
  majors = read_csv_column('data//roster_selected.csv', 'Major')
  counts_by_major = counts(majors)
  program_names = read_csv_dict('data//programs.csv', 'Code', 'Program Name')
  # ---
  by_count = items_v_k(counts_by_major)
  # ---
  by_count.sort(reverse=True) # from largest to smallest
  for count, code in by_count:
    program = program_names[code]
    print(count, program)  

if __name__ == '__main__':
  main()