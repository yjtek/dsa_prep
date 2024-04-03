# python3
from collections import deque 
from typing import Any

class Query:

    def __init__(self, query: list[str]) -> None:
        self.type: str= query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s: str = query[1]

class QueryProcessorOld:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count) -> None:
        self.bucket_count: Any = bucket_count
        # store all strings in one list
        self.elems: list[Any] = []

    def _hash_func(self, s: str) -> Any:
        ans = 0
        for c in reversed(s):
            ans: int = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found) -> None:
        print('yes' if was_found else 'no')

    def write_chain(self, chain) -> None:
        print(' '.join(chain))

    def read_query(self) -> Query:
        return Query(input().split())

    def process_query(self, query) -> None:
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind: int = self.elems.index(query.s)
            except ValueError:
                ind: int = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self) -> None:
        n = int(input())
        for _ in range(n):
            self.process_query(self.read_query())

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count) -> None:
        self.bucket_count: Any = bucket_count
        # store all strings in one list
        self.chains: dict[int, deque[Any]] = {chain_index: deque() for chain_index in range(bucket_count)}
        self.results: list[Any] = []

    def _hash_func(self, s) -> int:
        ans = 0
        for c in reversed(s):
            ans: int = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found) -> None:
        print('yes' if was_found else 'no')

    def write_chain(self, chain) -> None:
        self.results.append(' '.join(chain))

    def read_query(self) -> Query:
        return Query(input().split())

    def process_query(self, query) -> None:
        if query.type == "check":
            self.write_chain(self.chains[query.ind])

        elif query.type == 'add':
            chain_index = self._hash_func(query.s)
            if query.s not in self.chains[chain_index]:
                self.chains[chain_index].appendleft(query.s)

        elif query.type == 'find':
            chain_index = self._hash_func(query.s)
            if query.s not in self.chains[chain_index]:
                self.results.append('no')
            else:
                self.results.append('yes')

        elif query.type == 'del':
            chain_index: int = self._hash_func(query.s)
            if query.s in self.chains[chain_index]:
                self.chains[chain_index].remove(query.s)
        
        else:
            raise ValueError('Operation must be one of `add`, `check`, `find`, `del`')
            
    def process_queries(self) -> None:
        n = int(input())
        for _ in range(n):
            self.process_query(self.read_query())
        self.write_responses()
    
    def write_responses(self) -> None:
        print('\n'.join(self.results))

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
