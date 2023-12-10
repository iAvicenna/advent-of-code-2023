#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 01:20:16 2023

@author: avicenna
"""

#red, green, or blue

import numpy as np
from collections import Counter


def part1(path):

  color_to_condition = {"red":12, "green":13, "blue":14}

  # split each line into lists of subsets of cubes
  s = lambda x: [y.strip(' ') for y in x.split(":")[-1].split(";")]

  # for each subset check if number of cubes is less than or equal to max
  # forming a flat list of bools. finally check if all is True
  h = lambda l:\
    all([int(e1.strip(' ').split(' ')[0]) <=
         color_to_condition[e1.strip(' ').split(' ')[1]]
         for e0 in l for e1 in e0.split(',')])

  with open(path, "r") as fp:

    lines = list(map(s, map(str.strip, fp.readlines())))

  does_satisfy = list(map(h, lines))

  return sum([ind+1 for ind,x in enumerate(does_satisfy) if x])


def part2(path):

  colors = ["red", "green", "blue"]

  #same as part1
  s = lambda x: [y.strip(' ') for y in x.split(":")[-1].split(";")]

  #turn each subset into a dictionary mapping color name to count
  h = lambda l:\
    [{e1.strip(' ').split(' ')[1]:int(e1.strip(' ').split(' ')[0])
      for e1 in e0.split(',')} for e0 in l]

  # iterate through colors and in a list of dictionaries find the maximum
  # number encountered for a given color in that game using the list of
  # dictionaries formed above
  m = lambda l:\
    np.prod([max([e1[key] if key in e1 else 0 for e1 in l]) for key in colors])

  with open(path, "r") as fp:

    lines = list(map(s, map(str.strip, fp.readlines())))

  return sum(list(map(m, map(h, lines))))


if __name__ == "__main__":

  answer = part1("./inputs/test_input2_1.txt")
  print(f"part1 test answer is {answer}")

  answer = part1("./inputs/input2.txt")
  print(f"part1 answer is {answer}")

  answer = part2("./inputs/test_input2_1.txt")
  print(f"part2 test answer is {answer}")

  answer = part2("./inputs/input2.txt")
  print(f"part2 test answer is {answer}")
