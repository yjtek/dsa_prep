# Uses python3
import sys
sys.setrecursionlimit(999_999)

def fib_eff(n, fib_store={0:0, 1:1, 2:1}):
    if n in fib_store.keys():
        return fib_store.get(n)
    
    fib_store[n] = fib_eff(n-1) + fib_eff(n-2)
    return fib_store[n]

def fib_partial_sum(m, n, fib_store = {0:0, 1:1, 2:1}):
    
    '''
    use result from 2.1.4 that sum f_0 to f_n = f_{n+2} - 1
    '''
    assert m <= n, 'm < n not satisfied'
    diff = (fib_eff(n+2, fib_store) - 2) - (fib_eff(m+2-1, fib_store) - 2)
    return int(str(diff)[-1])


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_partial_sum(from_, to))
