'''
Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
'''

def countlen(num):
    if num//10 == 0:
        return 1
    else:
        return 1 + countlen(num//10)

if __name__ == '__main__':
    countlen(12214028)