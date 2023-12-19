import sys
sys.setrecursionlimit(999_999)

def fib_eff(n, fib_store={0:0, 1:1, 2:1}):
    if n in fib_store.keys():
        return fib_store.get(n)
    
    fib_store[n] = fib_eff(n-1) + fib_eff(n-2)
    return fib_store[n]

def fib_sum_last_digit_eff(n, fib_store = {0:0,1:1,2:1}):
    '''
    Note that sum of F0 ... FN is simply F_{N+2} - 1
    '''
    if n <= 1:
        return n
    
    if (n+2) not in fib_store.keys():
        fib_store[n+2] = fib_eff(n+1) + fib_eff(n)
    
    return int(str(fib_store[n+2] - 1)[-1])

if __name__ == '__main__':
    n = int(input())
    print(fib_sum_last_digit_eff(n))
