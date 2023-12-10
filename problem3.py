#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:32:09 2023

@author: avicenna
"""


import numpy as np
import re


def part1(path):

  '''
  quite direct way, turn the input into a char array
  search each line for numbers and when found, search a rectangle
  around this number slicing the char array with the condition there
  should be a symbol
  '''

  s = lambda x: x.strip().strip('\n')

  with open(path, "r") as fp:
    lines = list(map(s, fp.readlines()))

  len0 = len(lines)
  len1 = len(lines[0])

  chr_array = np.array(list(map(list, lines)))
  cond = np.vectorize(lambda x: not x.isnumeric() and x != '.')

  part_numbers = []

  for indline,line in enumerate(lines):

    r0 = max(indline-1, 0)
    r1 = min(indline+2, len0)

    for match in re.finditer("\d+", line):
      s0 = max(match.span()[0]-1, 0)
      s1 = min(match.span()[1]+1, len1)

      if np.any(cond(chr_array[r0:r1, s0:s1])):
        part_numbers.append(int(match.group()))


  return sum(part_numbers)


def part2(path):
  '''
  very similar to above but searching for * (gear) instead of any symbol
  and updating a dictionary which maps a coordinate to
  an empty list if there is no * with adjacent numbers at that position
  otherwise a list of adjacent numbers to that *
  '''

  s = lambda x: x.strip().strip('\n')

  with open(path, "r") as fp:
    lines = list(map(s, fp.readlines()))

  len0 = len(lines)
  len1 = len(lines[0])

  asterisk_adjacents = {(s0,s1):[] for s0 in range(len0) for s1 in range(len1)}

  chr_array = np.array(list(map(list, lines)))

  for indline,line in enumerate(lines):

    r0 = max(indline-1, 0)
    r1 = min(indline+2, len0)

    for match in re.finditer("\d+", line):
      s0 = max(match.span()[0]-1, 0)
      s1 = min(match.span()[1]+1, len1)

      I = np.argwhere(chr_array[r0:r1, s0:s1]=='*') + np.array([r0, s0])
      I = map(tuple, I)

      asterisk_adjacents.update({i:asterisk_adjacents[i]+[int(match.group())] for i in I})

  gear_adjacents = [np.prod(x) for x in asterisk_adjacents.values()
                    if len(x)==2]

  return np.sum(gear_adjacents)



if __name__ == "__main__":

  answer = part1("./inputs/test_input3_1.txt")
  print(f"part1 test answer is {answer}")

  answer = part1("./inputs/input3.txt")
  print(f"part1 answer is {answer}")

  answer = part2("./inputs/test_input3_1.txt")
  print(f"part2 test answer is {answer}")

  answer = part2("./inputs/input3.txt")
  print(f"part2 answer is {answer}")
