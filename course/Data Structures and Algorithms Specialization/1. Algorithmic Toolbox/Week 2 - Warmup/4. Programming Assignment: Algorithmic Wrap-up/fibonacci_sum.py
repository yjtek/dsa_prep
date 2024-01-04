def fib_sum_last_digit_naive(n):
    if n <= 1:
        return n
    
    fib_sum = 0
    f0, f1, _sum = 0, 1, 1

    for i in range(1, n):
        f0, f1 = f1, f0+f1 
        _sum += f1
    
    return int(str(_sum)[-1])

def get_pisano_period(m):
    prev, curr = 0, 1
    for i in range(m**2):
        prev, curr = curr, (prev+curr)%m
        if (prev == 0) & (curr == 1):
            return i+1

def fib_sum_last_digit_eff(n, fib_store = {0:0,1:1,2:1}):
    '''
    Note that sum of F0 ... FN is simply F_{N+2} - 1
    '''
    pisano_period = get_pisano_period(10)

    while n > 100:
        n = n % pisano_period

    if n <= 1:
        return n
    
    prev, curr = 0, 1
    
    for i in range(2, n+3):
        prev, curr = curr, prev+curr

    return (int(str(curr)[-1]) - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fib_sum_last_digit_eff(n))
