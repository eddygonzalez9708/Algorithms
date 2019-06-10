#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]

  choices = ['rock', 'paper', 'scissors']
  main = []

  def helper_func(main, start, end, copy):
    if start == end:
      return

    new_cpy = copy[:]

    for x in range(2):
      helper_func(main, start + 1, n, new_cpy)
      
      if new_cpy[start] == 'rock':
        new_cpy[start] = 'paper'
      elif new_cpy[start] == 'paper':
        new_cpy[start] = 'scissors'
        main.append(new_cpy[:])
        helper_func(main, start + 1, n, new_cpy)
        break
      else:
        new_cpy[start] = 'rock'
      
      main.append(new_cpy[:])

  for choice in choices:
    copy = [choice] + ['rock'] * (n - 1)
    main.append(copy)
    helper_func(main, 1, n, copy)

  return main

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')