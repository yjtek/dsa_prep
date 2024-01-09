import math
shortest_path = {}

def compute_operations_iter(n):
    if n < 1:
        return ([], 0)
    
    for i in range(1, n+1):
        if i % 3 == 0:
            div3_path, div3_pathlen = shortest_path.get(i/3, ([], 0))
        else:
            div3_path, div3_pathlen = (None, math.inf)

        if i % 2 == 0:
            div2_path, div2_pathlen = shortest_path.get(i/2, ([], 0))
        else:
            div2_path, div2_pathlen = (None, math.inf)
    
        minus1_path, minus1_pathlen = shortest_path.get(i-1, ([], 0))

        minlen = min(div3_pathlen, div2_pathlen, minus1_pathlen)
        if div3_pathlen == minlen:
            shortest_path[i] = ([i] + div3_path, div3_pathlen + 1)
        elif div2_pathlen == minlen:
            shortest_path[i] = ([i] + div2_path, div2_pathlen + 1)
        elif minus1_pathlen == minlen:
            shortest_path[i] = ([i] + minus1_path, minus1_pathlen + 1)
    
    return shortest_path[n][0][::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations_iter(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
