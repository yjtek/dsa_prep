def get_pisano_period(m):
    prev, curr = 0,1
    for i in range(m**2):
        prev, curr = curr, (prev+curr) % m
        if (prev == 0) & (curr == 1):
            return 2 + i - 1

def fib_partial_sum(m, n, fib_store = {0:0, 1:1, 2:1}):
    '''
    Since we only care about last digit, use the Pisano period approach to get the remainder when mod is 10. Then the difference between last digis D % 10 is the last digit
    '''
    pisano = get_pisano_period(10)
    m_mod = m+2-1
    n_mod = n+2
    
    while m_mod > 100:
        if m_mod == (m_mod % pisano):
            break
        m_mod = m_mod % pisano

    while n_mod > 100:
        if n_mod == (n_mod % pisano):
            break
        n_mod = n_mod % pisano
    
    diff = (fib_eff(n_mod, fib_store) - 1) - (fib_eff(m_mod, fib_store) - 1) % 10
    # print(curr_m, curr_n)
    return int(str(diff)[-1])

def fib_eff(n, fib_store={0:0, 1:1, 2:1}):
    if n in fib_store.keys():
        return fib_store.get(n)
    
    fib_store[n] = fib_eff(n-1) + fib_eff(n-2)
    return fib_store[n]

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fib_partial_sum(from_, to))

