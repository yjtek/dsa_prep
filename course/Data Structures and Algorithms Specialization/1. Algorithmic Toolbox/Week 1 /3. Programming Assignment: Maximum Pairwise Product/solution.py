def max_pairwise_product(a: list[float]) -> float:
    maxval_index = -1
    for i in range(len(a)):
        if ((maxval_index == -1) or (a[i] > a[maxval_index])):
            maxval_index = i

    maxval_index2 = -1
    for i in range(len(a)):
        if i == maxval_index:
            continue
        if ((maxval_index2 == -1) or (a[i] > a[maxval_index2])):
            maxval_index2 = i
    return a[maxval_index] * a[maxval_index2]

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))    
    print(max_pairwise_product(input_numbers))