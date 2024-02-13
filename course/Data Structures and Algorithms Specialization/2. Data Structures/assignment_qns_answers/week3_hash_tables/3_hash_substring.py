# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def PolyHash(text, polynomial=10, prime=1000000007):
    text_list = list(text)[::-1]
    hash_val = 0
    for char in text_list:
        hash_val = ((hash_val * polynomial) + ord(char)) % prime
    return hash_val

def PrecomputeHash(text, pattern, polynomial=10, prime=1000000007):
    pattern_len = len(pattern)
    text_len = len(text)

    last_substring = text[(text_len-pattern_len):text_len]
    last_substring_hash = PolyHash(last_substring, polynomial, prime)
    
    hash_values = [None] * (text_len-pattern_len+1)
    hash_values[-1] = last_substring_hash
    
    x_power_patternlen = 1
    for i in range(pattern_len):
        x_power_patternlen = (x_power_patternlen * polynomial) % prime 

    for i in range(text_len-pattern_len-1, -1, -1):
        hash_values[i] = (polynomial*hash_values[i+1] + ord(text[i]) - (ord(text[i + pattern_len]) *  x_power_patternlen)) % prime
    
    return hash_values

def RabinKarp(pattern, text, polynomial=123, prime=1000000007):
    hash_values = PrecomputeHash(text, pattern, polynomial=polynomial, prime=prime)
    pattern_hash = PolyHash(pattern, polynomial)
    positions = []

    for i in range(len(text) - len(pattern) + 1):
        # print(f"{i=}, {hash_values[i]=}")
        if hash_values[i] == pattern_hash:
            # print('here')
            if text[i:(i+len(pattern))] == pattern:
                positions.append(i)
    return positions

if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))

