from collections import namedtuple
from itertools import combinations
from math import sqrt, inf
# import numpy as np


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def minimum_distance_dnc(points_sorted, return_points: bool = False):
    if len(points_sorted) in [0,1]:
        if return_points:
            return inf, None, None
        return inf

    if len(points_sorted) == 2:
        if return_points:
            return distance_squared(points_sorted[0], points_sorted[1]), points_sorted[0], points_sorted[1]
        return distance_squared(points_sorted[0], points_sorted[1])
        
    mid_index = len(points_sorted)//2
    if return_points:
        min_dist_left, smallest_distance_point1, smallest_distance_point2 = minimum_distance_dnc(points_sorted[:mid_index])
        min_dist_right, smallest_distance_point1, smallest_distance_point2 = minimum_distance_dnc(points_sorted[mid_index:])
    else:
        min_dist_left = minimum_distance_dnc(points_sorted[:mid_index])
        min_dist_right = minimum_distance_dnc(points_sorted[mid_index:])

    min_dist = min(min_dist_left, min_dist_right)

    points_sorted_filtered = [p for p in points_sorted if abs(points_sorted[mid_index].x - p.x) <= min_dist]
    points_sorted_filtered = sorted(points_sorted_filtered, key=lambda p: p.y)

    for i in range(len(points_sorted_filtered)):
        for j in range(i+1, min(i+6, len(points_sorted_filtered))):
            if distance_squared(points_sorted_filtered[i], points_sorted_filtered[j]) < min_dist:
                #print(distance_squared(points_sorted_filtered[i], points_sorted_filtered[j]))
                min_dist = distance_squared(points_sorted_filtered[i], points_sorted_filtered[j])
                smallest_distance_point1 = points_sorted_filtered[i]
                smallest_distance_point2 = points_sorted_filtered[j]
    
    if return_points:
        return min_dist, smallest_distance_point1, smallest_distance_point2
    return min_dist

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    points_sorted = sorted(input_points, key=lambda p: (p.x, p.y))
    print("{0:.9f}".format(sqrt(minimum_distance_dnc(points_sorted))))
