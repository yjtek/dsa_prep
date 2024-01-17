import re
import math

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def maximum_value(dataset):
    digits = re.split('\-|\+|\*', dataset)
    ops = re.findall('\-|\+|\*', dataset)
    
    # every row represents a `start_index`, and every col represents an `end_index`
    # The value at (`start_index`, `end_index`) refers to the maximum possible value looking at the subarray of digits between the start and end indices
    # Since we have operations `+`, `-`, `*`, we need to store both the minimum and maximum possible values. Because, for example, a `-` operation is only maximised when the LHS subarray is maximised, and the RHS is minimised (assuming it is not negative)
    min_cache = [['' for _ in range(len(digits))] for _ in range(len(digits))]
    max_cache = [['' for _ in range(len(digits))] for _ in range(len(digits))]
    
    # We iterate through the cache diagonally, because at each value, we either fill it with the number that is directly above it (do not use the i-th value) or the one that is 1 row up and value(i) columns to the left
    for i in range(len(digits)):
        for j in range(len(digits)-i):
            # print('='*50)
            # print(f"{i=}, {j=}, {i+j=}")
            
            ## If we look at subarray of length 1, the only possible value is itself. 
            if j == i+j:
                min_cache[j][i+j] = digits[j]
                max_cache[j][i+j] = digits[j]
            
            ## Otherwise, if there is more than 1 digit, there is at least 1 way to add brackets. The idea here is that, for any composite array with 3 digits and above, you can split it into smaller subarrays with known values (e.g. with 3, you can split 1-2 or 2-1. With 4, you can split 1-3, 2-2, 3-1, and the 3 can be further split iteratively). The point is that the subarrays are of known values, so to find how to maximise any larger subarray, we just need to try 4 possible permutations of min and max for both the left and right subarrays
            else:
                minval = math.inf
                maxval = -math.inf

                for midpoint in range(j, i+j):
                    # print(f"{i=}, {j=}, {i+j=}, {midpoint=}")

                    minmin = eval(str(min_cache[j][midpoint]) + ops[midpoint] + str(min_cache[midpoint+1][i+j]))
                    maxmax = eval(str(max_cache[j][midpoint]) + ops[midpoint] + str(max_cache[midpoint+1][i+j]))
                    minmax = eval(str(min_cache[j][midpoint]) + ops[midpoint] + str(max_cache[midpoint+1][i+j]))
                    maxmin = eval(str(max_cache[j][midpoint]) + ops[midpoint] + str(min_cache[midpoint+1][i+j]))

                    minval = min(
                        minval,
                        minmin,
                        maxmax,
                        minmax,
                        maxmin, 
                    )

                    maxval = max(
                        maxval,
                        minmin,
                        maxmax,
                        minmax,
                        maxmin, 
                    )

                min_cache[j][i+j] = minval
                max_cache[j][i+j] = maxval

    return max_cache[0][len(digits)-1]

if __name__ == "__main__":
    print(maximum_value(input()))
