#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 01:20:16 2023

@author: avicenna
"""

import re


def part1(path):

  with open(path, "r") as fp:
    lines = list(map(str.strip, fp.readlines()))

  assert all([len([x for x in l if x.isnumeric()])>0 for l in lines])

  g = lambda l: [int(x) for x in l if x.isnumeric()][0]

  return sum([ 10*g(l) + g(l[::-1]) for l in lines])


def part2(path):

  with open(path, "r") as fp:
    lines = list(map(str.strip, fp.readlines()))

  expr = "(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))"
  f = lambda x: re.findall(expr, x, flags=re.IGNORECASE)

  r = lambda l: l.lower().replace("zero", "0").replace("one", "1").\
    replace("two", "2").replace("three", "3").replace("four", "4").\
      replace("five", "5").replace("six", "6").replace("seven", "7").\
        replace("eight", "8").replace("nine", "9")


  lines = [[r(e) for e in l] for l in map(f,lines)]

  return sum([ 10*int(l[0]) + int(l[-1]) for l in lines])


if __name__ == "__main__":

  answer = part1("./inputs/test_input1_1.txt")
  print(f"part1 test answer is {answer}")

  answer = part1("./inputs/input1.txt")
  print(f"part 1 answer is {answer}\n")


  answer = part2("./inputs/test_input1_2.txt")
  print(f"part2 test answer is {answer}")

  answer = part2("./inputs/input1.txt")
  print(f"part 2 answer is {answer}")
