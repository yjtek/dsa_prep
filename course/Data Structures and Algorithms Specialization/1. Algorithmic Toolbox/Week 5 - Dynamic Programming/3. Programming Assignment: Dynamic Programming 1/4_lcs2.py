def lcs2(seq1, seq2):
    seq1_split = [' '] + seq1
    seq2_split = [' '] + seq2

    mem = [[0 for _ in range(len(seq2_split))] for _ in range(len(seq1_split))]
    
    for i in range(len(seq1_split)):
        for j in range(len(seq2_split)):
            if i == 0 or j == 0:
                mem[i][j] = 0
                continue

            delete = mem[i-1][j] 
            insert = mem[i][j-1]
            match = mem[i-1][j-1] + 1

            if seq1_split[i]==seq2_split[j]:
                mem[i][j] = max(delete, insert, match)
            else:
                mem[i][j] = max(delete, insert)

    return mem[len(seq1_split)-1][len(seq2_split)-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
