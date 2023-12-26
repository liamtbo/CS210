"""calculating the cost per square inch
Author:  Liam Bouffard
Credits:  None
"""

import math
import doctest

def circle_area(diameter: float) -> float: 
  '''
  determines the area of a circle given the diameter
  
  >>> circle_area(4)
  12.566370614359172
  '''
  radius = diameter / 2
  circle_a = math.pi * radius ** 2

  return circle_a

# Pizza calculator example code  -- pizza_calculator.py
def pizza_calculator(diameter, cost): 
  ''' 
  (int, num) -> float 

  Calculates and returns the cost per square inch 
  of pizza for a pizza of given diameter andcost. 
  Examples: 

  >>> pizza_calculator(14, 18) 
  0.117
  >>> pizza_calculator(14, 20.25)  
  0.132
  ''' 
  area = circle_area(diameter)

  cost_per_inch = cost / area 
  cost_per_inch = round(cost_per_inch, 3) 
  return cost_per_inch

def main():
  print(doctest.testmod())

if __name__ == '__main__':
  main()
