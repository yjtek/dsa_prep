from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

def points_cover_sweepline(starts, ends, points):
    '''
    Time complexity: O(N+M log(N+M)) (see explainer above)
    Space complexity: O(M) for extra hashmap and return list
    '''

    starts_tup = [(x, 'l') for x in starts]
    ends_tup = [(x, 'r') for x in ends]
    points_tup = [(x, 'p') for x in points]
    sorted_array = sorted(starts_tup + ends_tup + points_tup, key = lambda x: (x[0], x[1]))

    nested_count = 0
    count_point_intersection = {}
    for element in sorted_array:
        if element[1] == 'l':
            nested_count+=1
        elif element[1] == 'r':
            nested_count-=1
        elif element[1] == 'p':
            count_point_intersection[element[0]] = nested_count

    retval = []
    for point in points:
        retval.append(count_point_intersection.get(point))
    
    return retval

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_sweepline(input_starts, input_ends, input_points)
    print(*output_count)
