from sys import stdin
import numpy as np

def optimal_value(capacity, weights, values):
    updated_capacity = capacity
    value_per_weight = [v/w for w,v in zip(weights,values)]
    total_value = 0
    while (updated_capacity != 0) and (len(value_per_weight) != 0):
        # print('='*50)
        max_index = np.argmax(value_per_weight)
        item_available_weight = weights.pop(max_index)
        item_value_per_weight = value_per_weight.pop(max_index)
        # print(item_available_weight)
        # print(item_value_per_weight)

        item_weight_added = min(item_available_weight, updated_capacity)
        # print(item_weight_added)


        updated_capacity -= item_weight_added
        # print(updated_capacity)

        total_value += (item_weight_added * item_value_per_weight)
        # print(total_value)

    return total_value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
