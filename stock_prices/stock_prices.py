#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_max_profit = None

  for x in range(len(prices)):
    for y in range(x + 1, len(prices)):
      val = prices[y] - prices[x]
      if (current_max_profit == None or val > current_max_profit):
        current_max_profit = val

  return current_max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))