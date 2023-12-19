def fib_last_digit(n):
    if n <= 1:
        return n

    n_minus_1 = 1
    n_minus_2 = 0
    
    for i in range(2, n+1):
        # print('='*50)
        # print(n_minus_1, n_minus_2)
        n_minus_1, n_minus_2 =  (n_minus_1+n_minus_2) % 10, n_minus_1
        # print(n_minus_1, n_minus_2)

    return n_minus_1


if __name__ == '__main__':
    n = int(input())
    print(fib_last_digit(n))
