from itertools import permutations
import numpy as np

def largest_number_naive(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            xy = str(numbers[i]) + str(numbers[j])
            yx = str(numbers[j]) + str(numbers[i])
            if xy <= yx:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return int(''.join([str(x) for x in numbers]))

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
