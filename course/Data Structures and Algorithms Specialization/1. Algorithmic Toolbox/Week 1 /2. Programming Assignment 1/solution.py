import argparse    

def sum_two_digits(a, b) -> float:
    assert 0 <= a <= 9, 'a out of bounds'
    assert 0 <= b <= 9, 'b out of bounds'
    return a + b

if __name__ == '__main__':
    a,b = input().split()
    a,b = int(a), int(b)
    sum_two_digits(a,b)

