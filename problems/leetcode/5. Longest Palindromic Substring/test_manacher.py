def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
        return
    N = 2*N+1    # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition
    R = 2     # centerRightPosition not inclusive
    i = 0    # currentRightPosition
    iMirror = 0     # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1
    
    # Let i be the rightmost position of the palindrome. Since the first viable center is position 1, 
    # the right edge of the palindrome is 2 by definition 
    for i in range(2,N): 
        
        # Find the mirror position of i around the center C. That is, if i is 2 away from center, then the mirror is 2 before C
        # Also written 2C-i by simplification.
        iMirror = C - (i - C) 
        
        #Let length of palindrome centered at i be 0
        L[i] = 0 
        
        ''' 
        This takes some explaining. Let's imagine some position i < R, such that diff > 0
        Let the left edge of the palindrome around C be L (the opposite edge from R)
        We know that iMirror is the mirror image of i around center C. 
        By symmetry, the distance of R from i must be the same as the distance of iMirror from L (R - i == iMirror - L)
        Let's suppose L[iMirror] == 10
        Let's suppose that distance of R from i is 3 
        Because 3 < 10, if we didn't have the `min` function, we would have ended up saying that there is palindrome of length
        10 centered at L[i]. However, this is not guaranteed!  The only reason why we can conclude that there is a palindrome of
        at least length R - i is because we already know that there is one between L-C-R.
        Hence, the length of any new palindrome MUST be bound by diff.
        Note that it is possible for a palindrome to exist at i that exceeds R. It is just not possible to pre-emptively confirm
        without checking
        '''
        diff = R - i 
        if diff > 0:
            L[i] = min(L[iMirror], diff)
   
        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE
        # If even position, we just increment LPS by ONE without
        # any character comparison
        try:
            # print(f'(i + L[i]) < N || ({i} + {L[i]}) < {N}')
            # print(f'((i - L[i]) > 0 || ({i} - {L[i]}) > 0')
            # print(f'((i + L[i] + 1) % 2 == 0) || (({i} + {L[i]} + 1) % 2 == 0)')
            # print(f'(text[(i + L[i] + 1) // 2] == text[(i - L[i] - 1) // 2]) || \
                #   (text[({i} + {L[i]} + 1) // 2] == text[({i} - {L[i]} - 1) // 2]) \
                #   ({text[(i + L[i] + 1) // 2]} == {text[(i - L[i] - 1) // 2]}) ')
            while (
                ((i + L[i]) < N) &
                ((i - L[i]) > 0) &
                (((i + L[i] + 1) % 2 == 0) or \
                 (text[(i + L[i] + 1) // 2] == text[(i - L[i] - 1) // 2]))
            ):
                L[i]+=1
        except Exception as e:
            pass
        
        if L[i] > maxLPSLength:        # Track maxLPSLength
            # print(f'L[i] > maxLPSLength ||  {L[i]} > {maxLPSLength}')
            maxLPSLength = L[i]
            maxLPSCenterPosition = i
   
        # If palindrome centered at currentRightPosition i
        # expand beyond centerRightPosition R,
        # adjust centerPosition C based on expanded palindrome.
        if i + L[i] > R:
            # print(f'i + L[i] > R ||  {i}+ {L[i]} > {R}')
            C = i
            R = i + L[i]
   
    # Uncomment it to print LPS Length array
    # printf("%d ", L[i]);
    start = (maxLPSCenterPosition - maxLPSLength) // 2
    end = start + maxLPSLength - 1
    # print ("LP S of string is " + text + " : ",text[start:end+1])
    return text[start:end+1]

if __name__ == '__main__':
    lps = findLongestPalindromicString('abaddab')
    