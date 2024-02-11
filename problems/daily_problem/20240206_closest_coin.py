'''
You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance. That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, coins are o, and empty spaces are . (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------
return (0, 4), since that coin is closest. This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
'''

import math

def manhattan_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    distance = abs(x1-x2) + abs(y1-y2)
    return distance

def closest_coin(my_position: tuple[int, int], coin_positions: list[tuple[int, int]]) -> tuple[int, int]:
    '''
    To get to closest coin, we must scan all coin positions. So time complexity cannot be anything less than O(N)
    '''
    
    closest_coins = []
    min_dist = math.inf
    for coin_pos in coin_positions:
        coin_dist = manhattan_distance(my_position, coin_pos)
        if coin_dist < min_dist:
            closest_coins = [coin_pos]
            min_dist = coin_dist
        elif coin_dist == min_dist:
            closest_coins.append(coin_pos)
    
    return closest_coins