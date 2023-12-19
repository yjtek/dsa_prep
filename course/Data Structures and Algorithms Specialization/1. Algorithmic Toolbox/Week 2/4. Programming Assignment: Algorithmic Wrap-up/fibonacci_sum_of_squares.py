import sys
sys.setrecursionlimit(999_999)

def fib_eff(n, fib_store={0:0, 1:1, 2:1}):
    if n in fib_store.keys():
        return fib_store.get(n)
    
    fib_store[n] = fib_eff(n-1) + fib_eff(n-2)
    return fib_store[n]

def fib_sum_squares_last_digit(n, fib_store={0:0, 1:1, 2:1}):
    '''
    Using hint in question, f6 * f5 = f1**2 + f2**2 + f3**2 + f4**2 + f5**2.
    In general, f_{n} * f_{n-1} = \sum_{i=0}^{n-1} f_{i}**2
    '''
    sum_squares = fib_eff(n+1, fib_store) * fib_eff(n, fib_store)
    return int(str(sum_squares)[-1])

if __name__ == '__main__':
    n = int(input())
    print(fib_sum_squares_last_digit(n))
