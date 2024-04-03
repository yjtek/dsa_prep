# python3

import sys

class Solver:
    def __init__(self, s) -> None:
        self.s: str = s
        self.polynomial=10
        self.prime1 = 1e9+7
        self.prime2 = 1e9+9
        self.precompute_hash_1 = self.compute_hash(string=s, polynomial=self.polynomial, prime=self.prime1)
        self.precompute_hash_2 = self.compute_hash(string=s, polynomial=self.polynomial, prime=self.prime2)

    def _ask(self, a, b, l):
        return self.s[a:(a+l)] == self.s[b:(b+l)]
    
    def polyhash(self, string, polynomial=10, prime=1e9+7):
        hashval = 0
        for char in string[::-1]:
            hashval += (((polynomial * hashval) % prime) + ord(char)) % prime
        return hashval
    
    def compute_hash(self, string, polynomial=10, prime=1e9+7):
        precompute_substring_hash = [0.] * (len(string)+1)
        for i in range(len(string)):
            precompute_substring_hash[i+1] = (
                (precompute_substring_hash[i] * polynomial) % prime + ord(string[i])
            ) % prime
        # print(precompute_substring_hash)
        return precompute_substring_hash

    def ask(self, a, b, l):
        polynomial_multiple1 = (self.polynomial**l) % self.prime1
        polynomial_multiple2 = (self.polynomial**l) % self.prime2
        
        hash1_a = (self.precompute_hash_1[a+l] - (polynomial_multiple1 * self.precompute_hash_1[a]) % self.prime1) % self.prime1
        hash2_a = (self.precompute_hash_2[a+l] - (polynomial_multiple2 * self.precompute_hash_2[a]) % self.prime2) % self.prime2

        hash1_b = (self.precompute_hash_1[b+l] - (polynomial_multiple1 * self.precompute_hash_1[b]) % self.prime1) % self.prime1
        hash2_b = (self.precompute_hash_2[b+l] - (polynomial_multiple2 * self.precompute_hash_2[b]) % self.prime2) % self.prime2
        
        hash1_match = hash1_a == hash1_b
        hash2_match = hash2_a == hash2_b

        return 'Yes' if hash1_match and hash2_match else 'No'
    
s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
