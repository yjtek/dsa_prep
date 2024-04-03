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

def polyhash(text, polynomial = 10, prime = 1e9+7):
    '''
    Time complexity: O(N) where N is the length of the text
    '''
    hashval = 0
    for char in text[::-1]:
        hashval = (((hashval * polynomial) % prime) + ord(char)) % prime
    return hashval

def precompute_hash(text, pattern, polynomial = 10, prime = 1e9+7):
    '''
    Time complexity: 
        - O(M) for computing the last item in the substring_hash_store
        - O(M) for computing x^p
        - O(N-M) for computing the rest of the hash store
        - Total: O(M+M+N-M) = O(M+N)
    '''
    ## Declare an array to hold the hash values of the substrings. 
    ## The length should be len(text) - len(pattern) + 1
    textlen = len(text)
    patternlen = len(pattern)
    
    count_valid_substrings = textlen - patternlen + 1
    
    substring_hash_store = [0.] * count_valid_substrings
    
    ## Compute hash of last possible substring at the end of text
    substring_hash_store[-1] = polyhash(text[count_valid_substrings-1:])

    ## Compute x^|P|
    x_power_p = 1
    for _ in range(len(pattern)):
        x_power_p = (x_power_p * polynomial) % prime

    ## Use recursive relation in a loop, to find the value of each 
    ## substring hash: 
    ## H[i] = (x * H[i+1] + T[i] - T[i + |P|] * x^|P|) mod p
    for i in range(count_valid_substrings-2, -1, -1):
        substring_hash_store[i] = (
            ((polynomial * substring_hash_store[i+1]) % prime) + 
            (ord(text[i]) % prime) -
            ((ord(text[i + len(pattern)]) * x_power_p) % prime)
        ) % prime
    
    return substring_hash_store 

def rabin_karp(text, pattern):
    '''
    Time complexity: 
        - O(M) for computing pattern hash
        - O(N+M) for precomputing hashes for text
        - The loop is slightly complex:
            - O((N-M+1)) for loop over all possible substrings
            - Assuming `q` hashes match and ignoring collisions, it is possible to incur q*M for each loop to check for string equality
            - Total: O(N-M+1 + qM) = O(N-M+1) assuming q is small
                - Worst case for q is N, so this can become O(N-M+1 + N*M) = O(N*M)
        - Total: O(M+N+M+N-M+1) = O(M+2N+1) = O(M+N)
    '''
    pattern_hash = polyhash(pattern)
    precomputed_hash = precompute_hash(text, pattern)
    result = []
    for i in range(len(text)-len(pattern)+1):
        if precomputed_hash[i] == pattern_hash:
            if text[i:(i+len(pattern))] == pattern:
                result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))

