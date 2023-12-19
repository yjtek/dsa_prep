def gcd(a, b):
    '''
    Using result from Euclidean method 
    '''
    if a < b:
        a,b = b,a

    if a % b == 0:
        return min(a,b)
    else:
        return gcd(b, a%b)

def lcm(a, b):
    '''
    - LCM and GCD have an interesting relationship.
    - Suppose gcd(a, b) = x. That means that 
        - a = x * f_1 * f_2 * ... f_n 
        - b = x * g_1 * g_2 * ... g_n 
        - where f_i and g_j are prime factors
    - Since x is gcd, it MUST be the case that f_1 ... f_n are distinct from g_1 ... g_n. 
        - Because if they are not distinct, the terms can be folded into the gcd!

    - So this means that the LCM must be
        - (a * b)/x = x * f_1 ... * f_n * g_1 * ... g_n
    '''
    x = gcd(a,b)
    
    return int((a*b)/x)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

