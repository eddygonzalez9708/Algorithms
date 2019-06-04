#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement a solution that is more efficient than the naive recursive solution.

# Pattern Found - 1 1 2 4 7 13 24 44 81 149 274

def eating_cookies(n, cache=None):
  if cache == None:
    cache = [0 for i in range(n + 1)]
  
  if n == 0 or n == 1:
    return 1
  elif n == 2:
    return 2

  cache[0] = 1
  cache[1] = 1
  cache[2] = 2

  for num in range(3, n + 1):
    cache[num] = sum(cache[num - 3:num])
  
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')