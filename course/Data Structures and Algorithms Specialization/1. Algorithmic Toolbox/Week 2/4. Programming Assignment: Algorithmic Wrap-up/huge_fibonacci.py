import sys
sys.setrecursionlimit(999_999)

def fib_eff(n, fib_store={0:0, 1:1, 2:1}):
    if n in fib_store.keys():
        return fib_store.get(n)
    
    fib_store[n] = fib_eff(n-1) + fib_eff(n-2)
    return fib_store[n]

def fib_eff_mod(n, m, fib_store={0:0, 1:1, 2:1}):
    if n in fib_store.keys():
        return fib_store.get(n)
    
    fib_store[n] = fib_eff(n-1, fib_store) + fib_eff(n-2, fib_store)
    return fib_store[n] % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fib_eff_mod(n, m))
