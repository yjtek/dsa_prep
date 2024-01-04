from itertools import permutations
import numpy as np

def max_dot_product(prices, clicks):
    assert len(prices) == len(clicks)
    prices = sorted(prices, reverse=True)
    clicks = sorted(clicks, reverse=True)
    
    return sum([p*c for p, c in zip(prices, clicks)])

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
