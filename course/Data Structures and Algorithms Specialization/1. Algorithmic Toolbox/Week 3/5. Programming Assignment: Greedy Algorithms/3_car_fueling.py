from sys import stdin
import numpy as np

def min_refills(distance_between_cities, distance_on_full_tank, stops):
    stops_remaining = stops
    curr_position = 0
    count_stops = 0

    while (len(stops) != 0) and ((curr_position + distance_on_full_tank) < distance_between_cities):
        try:
            travel_till_index = np.argmax([x for x in stops_remaining if (x-curr_position) <= distance_on_full_tank])
        except:
            break

        curr_position = stops_remaining[travel_till_index]
        stops_remaining = stops_remaining[(travel_till_index+1):]
        count_stops += 1
    
    if (curr_position + distance_on_full_tank) >= distance_between_cities:
        return count_stops
    else:
        return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
