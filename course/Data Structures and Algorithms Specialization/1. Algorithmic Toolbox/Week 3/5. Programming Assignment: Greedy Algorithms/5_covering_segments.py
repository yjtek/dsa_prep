from sys import stdin
from collections import namedtuple
import numpy as np

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments_sort_left_bound = sorted(segments, key=lambda x: x[0]) 

    prev_segment = None
    curr_segment = None
    right_bound = -1
    points = [] 
    
    # print(segments_sort_left_bound)
    while len(segments_sort_left_bound) != 0:
        # print('='*50)
        # print(f'{segments_sort_left_bound=}')
        # print(f'{prev_segment=}')
        # print(f'{curr_segment=}')
        
        if (curr_segment is None) & (prev_segment is None):
            prev_segment = segments_sort_left_bound.pop(0)
            right_bound = prev_segment[1]
            
        curr_segment = segments_sort_left_bound.pop(0)
        
        # print(f'{segments_sort_left_bound=}')
        # print(f'{prev_segment=}')
        # print(f'{curr_segment=}')
        # print(f'{right_bound=}')
        # print(f'{points=}')

        if curr_segment[0] > right_bound:
            prev_segment, curr_segment = curr_segment, None
            points.append(right_bound)
            right_bound = prev_segment[1] 
        elif curr_segment[1] < right_bound:
            right_bound = curr_segment[1]

    points.append(right_bound)
    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
