def fib_last_digit(n):
    if n <= 1:
        return n

    curr = 1
    prev = 0
    
    for i in range(2,n+1):
        # print(prev, curr, (prev+curr) % 10)
        prev, curr = curr, (prev+curr) % 10
    
    return curr


if __name__ == '__main__':
    n = int(input())
    print(fib_last_digit(n))
