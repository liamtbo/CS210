"""Estimate the value of Pi with Monte Carlo simulation.
Author:  Liam Bouffard
Credits:  None
"""
import random
import doctest
from turtle import color
import points_plot
import math

GOOD_PI = 3.141592653589793
SAMPLES = 5_000

def in_unit_circle(x: float, y: float) -> bool:
  '''Returns True if and only if (x, y) lies within circle with origin (0, 0) and radius 1.0

  >>> in_unit_circle(0.0, 0.0)
  True
  >>> in_unit_circle(1.0, 1.0)
  False
  >>> in_unit_circle(0.5, -0.5)
  True
  >>> in_unit_circle(-0.9, -0.5)
  False
  '''
  if math.sqrt((x**2 + y**2)) <= 1.0:
    within_circle = True
  else:
    within_circle = False
  return within_circle

def rand_point_unit_sq() -> tuple[float, float]:
  '''Returns random x, y both in range 0..1.0, 0..1.0.'''
  x = random.random()
  y = random.random()
  return x, y

def plot_random_points(n_points: int = 500):
  '''Generate and plot n_points points in interval (0, 0) to (1, 1)'''
  points_plot.init()
  # problem - graph is inverted for whatever reason
  for i in range(n_points):
    x, y = rand_point_unit_sq()
    if in_unit_circle(x, y):
      points_plot.plot(x, y, color_rgb=(50, 50, 168)) # blue
    else:
      points_plot.plot(x, y, color_rgb=(168, 50, 149)) # purple
  points_plot.wait_to_close()



def relative_error(est: float, expected: float) -> float:
  '''Relative error of estimte (est) as non-negative fraction of exected value.
  >>> round(relative_error(3.0, 5.0), 2)
  0.4
  >>> round(relative_error(5.0, 3.0), 2)
  0.67
  '''
  abs_error = est - expected
  rel_error = abs(abs_error / expected)
  return rel_error

def pi_approx() -> float:
  '''Return an estimate of pi by sampling random points.
  >>> relative_error(pi_approx(), GOOD_PI) <= 0.01 # within 1%
  True
  >>> relative_error(pi_approx(), GOOD_PI) <= 0.01 # within 1%
  True
  >>> relative_error(pi_approx(), GOOD_PI) <= 0.01 # within 1%
  True
  '''
  total_tried = 0
  in_circle = 0
  for iter in range(SAMPLES):
    x, y = rand_point_unit_sq()
    total_tried += 1
    if in_unit_circle(x, y):
      in_circle += 1
    else:
      None
  pi_est = (in_circle / total_tried) * 4
  return pi_est


def main():
  doctest.testmod()
  plot_random_points(SAMPLES)
  estimate = pi_approx()
  print(f'Pi is approximately {estimate}')

if __name__ == "__main__":
  main()
