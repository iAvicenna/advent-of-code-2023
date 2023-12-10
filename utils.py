#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:17:01 2023

@author: avicenna
"""

from interval import interval as _int, inf


def complement(interval):

  '''
  required for defining set theoretic difference
  for integer based intervals
  '''

  complement = []

  if len(interval)==0:
    return _int([-inf,inf])
  if interval == _int([-inf,inf]):
    return _int()


  for ind in range(len(interval)):

    if ind==0:
      if interval[ind].inf != -inf:
        complement.append([-inf, interval[ind].inf-1])

    if ind==len(interval)-1:
      if interval[ind].inf != inf:
        complement.append([interval[ind].sup+1, inf])

    else:
      if interval[ind].sup+1<=interval[ind+1].inf-1:
        complement.append([interval[ind].sup+1,
                           interval[ind+1].inf-1])

  return _int(*complement)


def difference(interval1, interval2):

  """
  interval library does not define difference
  interval1/interval2
  """
  return interval1 & complement(interval2)


class PointedInterval():
  '''
  derives from the interval class, pointed means each interval that
  makes up the whole interval also has an associated point which is used
  to define the relevant mapping in question 5
  '''

  def __init__(self, intervals, points):

    assert len(intervals) == len(points)

    self.points = points
    self.interval = _int(*intervals)
    self._intervals = [_int[x[0],x[1]] for x in intervals]

  def add_points(self, points):
    assert len(points) == self.ninput_intervals

  def index(self, x):

    I = [ind for ind,interval in enumerate(self._intervals) if
         _int(x) in _int(interval)]

    if len(I) == 0:
      return None
    else:
      return I[0]

  def intersections(self, x):

    I = [ind for ind,interval in enumerate(self._intervals) if
         len(_int(x) & _int(interval))!=0]

    return I

  def map(self, x):

    ind = self.index(x)

    if ind is None: return x

    return int(self.points[ind] + x - self._intervals[ind][0].inf)

  def map_interval(self, interval):

    intersection = self.interval & interval
    remaining = difference(interval, intersection)
    targets = []

    for elem in intersection:
      I = self.intersections(elem)

      if len(I)==0:
        targets.append(elem)
        continue

      for ind in I:
        s0 = int(self.points[ind] + elem.inf - self._intervals[ind][0].inf)
        s1 = int(self.points[ind] + elem.sup - self._intervals[ind][0].inf)
        targets.append([s0, s1])

    for elem in remaining:
      targets.append(elem)

    return _int(*targets)


if __name__ == "__main__":

  #test for pointed interval

  interval = PointedInterval([[1,3],[4,6]], [1,2])
  assert interval.index(2)==0
  assert interval.index(1.5)==0
  assert interval.index(2.5)==0
  assert interval.index(4)==1
  assert interval.index(6.1) is None
  assert interval.map(2) == 2
  assert interval.map(6) == 4

  complement(_int([2.0, 3.0], [4.0, 6.0]))

  assert complement(_int([5,6], [1,2])) == _int([-inf, 0.0], [3.0, 4.0], [7.0, inf])
  assert difference(_int([5,6], [1,2]), _int([5,6])) == _int([1.0, 2.0])

  assert interval.map_interval(_int([2,7])) == _int([2.0, 4.0], [7.0])
