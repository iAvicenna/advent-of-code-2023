#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:32:09 2023

@author: avicenna
"""


import numpy as np
import re
import numpy as np


def part1(path):
  '''
  iterate over lines, split them accordingly and look at the intersection
  of winning and my numbers
  '''

  s = lambda x: x.strip().strip('\n')

  with open(path, "r") as fp:
    lines = list(map(s, fp.readlines()))

  score = 0

  s = lambda x,i: [e for e in x.split(': ')[1].split(' | ')[i].split(' ')
                   if e !='']

  for line in lines:

    winning_numbers = list(map(int, s(line, 0)))
    my_numbers = list(map(int, s(line, 1)))
    common_numbers = set(my_numbers).intersection(winning_numbers)
    nwinning = sum([my_numbers.count(x) for x in common_numbers])

    if nwinning>0: score += 2**(nwinning-1)


  return score


def part2(path):

  '''
  similar to above but keep an array of extra weights which is updated
  whenever there are winning numbers.
  '''

  s = lambda x: x.strip().strip('\n')

  with open(path, "r") as fp:
    lines = list(map(s, fp.readlines()))

  s = lambda x,i: [e for e in x.split(': ')[1].split(' | ')[i].split(' ')
                   if e !='']

  extra_copies = np.zeros((len(lines)))

  for indl,line in enumerate(lines):

    winning_numbers = list(map(int, s(line, 0)))
    my_numbers = list(map(int, s(line, 1)))
    common_numbers = set(my_numbers).intersection(winning_numbers)
    nwinning = sum([my_numbers.count(x) for x in common_numbers])

    extra_copies[indl+1:min(indl+1+nwinning, len(lines))] +=\
      (1+extra_copies[indl])

  return int(len(lines) + np.sum(extra_copies))


if __name__ == "__main__":

  answer = part1("./inputs/test_input4_1.txt")
  print(f"part1 test answer is {answer}")

  answer = part1("./inputs/input4.txt")
  print(f"part1 answer is {answer}")

  answer = part2("./inputs/test_input4_1.txt")
  print(f"part2 test answer is {answer}")

  answer = part2("./inputs/input4.txt")
  print(f"part2 answer is {answer}")
