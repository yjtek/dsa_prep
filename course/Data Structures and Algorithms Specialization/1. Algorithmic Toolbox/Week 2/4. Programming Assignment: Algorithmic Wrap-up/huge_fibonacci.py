import sys
sys.setrecursionlimit(999_999)

def fib_eff(n, fib_store={0:0, 1:1, 2:1}):
    if n in fib_store.keys():
        return fib_store.get(n)
    
    fib_store[n] = fib_eff(n-1) + fib_eff(n-2)
    return fib_store[n]

def get_pisano_period(m):
    prev, curr = 0, 1
    for i in range(m**2):
        prev, curr = curr, (prev+curr)%m
        if (prev == 0) & (curr == 1):
            return i+1

def fib_huge_mod(N, m, fib_store={0:0, 1:1, 2:1}):
    pisano_period = get_pisano_period(m)
    # print(pisano_period)

    while N > 100:
        if N == (N % pisano_period):
            break
        N = N % pisano_period
    
    if N in fib_store.keys():
        return fib_store[N] % m
    else:
        fib_store[N] = fib_eff(N-1, fib_store) + fib_eff(N-2, fib_store)

    return fib_store[N] % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fib_huge_mod(n, m))
