'''Summarize a path in a map, using the standard Ramer-Douglas-Peucher (aka Dude-Hard)
split-and-merge algorithm
Authos: Liam Bouffard
Credits: None
'''
import csv
import doctest
import geometry
import map_view
import config

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def read_points(path: str) -> list[tuple[float, float]]:
  '''retrieves east north data from a csv file'''
  with open(path, 'r') as csvFile:
    csv_reader = csv.reader(csvFile)
    cuml = 0
    e_n_list = []
    for east, north in csv_reader:
      cuml += 1
      if cuml != 1:
        e_n_list.append((float(east), float(north)))
  return e_n_list

def summarize(points: list[tuple[float, float]],
              tolerance: int = config.TOLERANCE_METERS,
              ) -> list[tuple[float, float]]:
  '''
  >>> path = [(0,0), (1,1), (2,2), (2,3), (2,4), (3,4), (4,4)]
  >>> expect = [(0,0), (2,2), (2,4), (4,4)]
  >>> simple = summarize(path, tolerance=0.5)
  >>> simple == expect
  True
  '''
  summary: list[tuple[float, float]] = [points[0]]
  epsilon = float(tolerance * tolerance)

  def simplify(start: int, end: int):
    '''Add necessary points in (start, end) to summary'''
    # graphs each start - end line
    # if end - start > 2:
      # map_view.scratch(points[start], points[end])

    # retreives the farthest from line point index
    farthest = start
    for point in range(start, end+1):
      if geometry.deviation_sq(points[start], points[end], points[point]) > epsilon:
        if geometry.deviation_sq(points[start], points[end], points[point]) > geometry.deviation_sq(points[start], points[end], points[farthest]):
          farthest = point

    # base case
    if farthest == start:
      summary.append(points[end])
      map_view.plot_to(points[point])
    
    # recursive case
    else:
      simplify(start, farthest)
      simplify(farthest, end)

    # return
  
  simplify(0, len(points) - 1)
  return summary



def main():
  map_view.init()
  points = read_points(config.UTM_CSV)
  print(f'{len(points)} raw points')
  summary = summarize(points, config.TOLERANCE_METERS)
  print(f'{len(summary)} points in summary')
  map_view.wait_to_close()

if __name__ == '__main__':
  doctest.testmod()
  print('Tested')
  main()