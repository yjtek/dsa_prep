import numpy as np

def optimal_summands(n) -> list:
    guess = n
    lb = 1
    ub = guess
    sumval_np1 = ((guess+1) * (guess+2))/2
    sumval = (guess * (guess+1))/2
    
    i = 0
    while not ((sumval <= n) and (sumval_np1 > n)):
        # print('='*50)
        # print(f'{ub=}')
        # print(f'{lb=}')
        # print(f'{guess=}')
        # print(f'{sumval=}')
        # print(f'{sumval_np1=}')
        # print(f'target={n}')        
        
        if (sumval > n):
            ub = (lb+ub) // 2 
        elif (sumval_np1 < n):
            lb = guess

        if guess == ((lb + ub) // 2):
            guess += 1
        else:
            guess = (lb + ub) // 2
        
        sumval_np1 = ((guess+1) * (guess+2))/2
        sumval = (guess * (guess+1))/2
        
    # print(f'while loop terminated at: {guess}')
    # print(sumval)
    # print(sumval_np1)
    # print(n)
    
    if sumval == n:
        return list(np.arange(guess) + 1)
    elif sumval < n:
        returnval = list(np.arange(guess) + 1)
        returnval[-1] += int(n - sumval)
        return returnval

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
