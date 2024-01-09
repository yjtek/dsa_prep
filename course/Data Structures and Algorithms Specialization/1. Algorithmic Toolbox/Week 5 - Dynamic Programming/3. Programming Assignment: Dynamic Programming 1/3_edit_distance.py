def edit_distance(str1, str2):
    str1_split = [' '] + list(str1)
    str2_split = [' '] + list(str2)
    mem = [[0 for _ in range(len(str2_split))] for _ in range(len(str1_split))]
    
    for i in range(len(str1_split)):
        for j in range(len(str2_split)):
            if i == 0:
                mem[i][j] = j
                continue
            if j == 0:
                mem[i][j] = i
                continue

            insert = mem[i-1][j] + 1
            delete = mem[i][j-1] + 1
            mismatch = mem[i-1][j-1] + 1
            match = mem[i-1][j-1]

            if str1_split[i] == str2_split[j]:
                mem[i][j] = min(match, insert, delete)
            elif str1_split[i] != str2_split[j]:
                mem[i][j] = min(mismatch, insert, delete)
            
    return mem[len(str1_split)-1][len(str2_split)-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
