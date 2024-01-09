def lcs3(seq1, seq2, seq3):
    seq1_split = [' '] + seq1
    seq2_split = [' '] + seq2
    seq3_split = [' '] + seq3 

    mem = [[[0 for _ in range(len(seq3_split))] for _ in range(len(seq2_split))] for _ in range(len(seq1_split))]

    for i in range(len(seq1_split)):
        for j in range(len(seq2_split)):
            for k in range(len(seq3_split)):
                if (i == 0) or (j == 0) or (k == 0):
                    mem[i][j][k] = 0
                    continue
                
                if (seq1_split[i] == seq2_split[j]) and (seq1_split[i] == seq3_split[k]):
                    mem[i][j][k] = mem[i-1][j-1][k-1] + 1
                else:
                    ## if current character does not match across 3 strings, the longest subsequence is the longest subsequence that exists when I remove a letter from one/two/three of my strings
                    ## In fact, this can be optimised further! We actually only need to consider the cases where we rmeove 1 letter from each string. Why? Because the maximum length of common subsequence 
                    ## between sequences of lengths (x-1, x, x) must be AT MOST the sequences of lengths (x-1, x-1, x)
                    mem[i][j][k] = max(
                        mem[i-1][j][k],
                        mem[i][j-1][k],
                        mem[i][j][k-1],

                        # mem[i-1][j-1][k],
                        # mem[i][j-1][k-1],
                        # mem[i-1][j][k-1],

                        # mem[i-1][j-1][k-1],
                    )

    return mem[len(seq1_split)-1][len(seq2_split)-1][len(seq3_split)-1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
