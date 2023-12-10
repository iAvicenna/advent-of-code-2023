#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 01:20:16 2023

@author: avicenna
"""
import time
from utils import PointedInterval
from interval import interval as _int


def solve(path, part):

  s = lambda x: x.strip().strip('\n')

  with open(path, "r") as fp:
    lines = list(map(s, fp.readlines()))

  if part==2:
    seed_info = list(map(int,lines[0].split(': ')[1].split(' ')))
    seed_interval = _int(*[[int(a), int(a+b)] for a,b in
                           zip(seed_info[::2], seed_info[1::2])])

  elif part==1:
    seed_interval = _int(*list(map(int,lines[0].split(': ')[1].split(' '))))



  I = [ind+2 for ind,line in enumerate(lines[2:]) if line == '']
  if lines[2:] != '': I = [1] + I
  if lines[-1] != '': I = I + [len(lines)]

  maps = [lines[i0+1:i1] for i0,i1 in zip(I[:-1],I[1:])]

  keys = ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water',
          'water_to_light', 'light_to_temperature', 'temperature_to_humidity',
          'humidity_to_location']

  v = {key:[] for key in keys}
  m = {key:[] for key in keys}


  for info in maps:
    key = info[0].split(' ')[0].replace('-','_')

    for data in info[1:]:
      d0 = int(data.split(' ')[0])
      s0 = int(data.split(' ')[1])
      n = int(data.split(' ')[2])

      m[key].append([s0, s0+n-1])
      v[key].append(d0)

  for key in m:
    m[key] = PointedInterval(m[key], v[key])

  for key in m:
    seed_interval = m[key].map_interval(seed_interval)

  return int(seed_interval[0].inf)


if __name__ == "__main__":

  t0 = time.time()
  answer = solve("./inputs/test_input5_1.txt", 1)
  t1 = time.time()
  print(f"part1 test answer is {answer} ({t1-t0:.2f} seconds)")

  t0 = time.time()
  answer = solve("./inputs/input5.txt", 1)
  t1 = time.time()
  print(f"part1 answer is {answer} ({t1-t0:.2f} seconds)")

  t0 = time.time()
  answer = solve("./inputs/test_input5_1.txt", 2)
  t1 = time.time()
  print(f"part2 test answer is {answer} ({t1-t0:.2f} seconds)")

  t0 = time.time()
  answer = solve("./inputs/input5.txt", 2)
  t1 = time.time()
  print(f"part2 answer is {answer} ({t1-t0:.2f} seconds)")
