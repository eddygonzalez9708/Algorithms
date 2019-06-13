#!/usr/bin/python

import sys

def making_change(amount, denominations):
  cache = { 0: 1 }

  for a in range(denominations[0], amount + 1):
    cache[a] = cache[a - 1]

  for b in range(denominations[1], amount + 1):
    cache[b] = cache[b] + cache[b - denominations[1]]

  for c in range(denominations[2], amount + 1):
    cache[c] = cache[c] + cache[c - denominations[2]]

  for d in range(denominations[3], amount + 1):
    cache[d] = cache[d] + cache[d - denominations[3]]

  for e in range(denominations[4], amount + 1):
    cache[e] = cache[e] + cache[e - denominations[4]]
  
  return cache[amount] 

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")