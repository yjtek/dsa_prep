# python3

import sys


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst, verbose=False):
        # if verbose:
        #     print('='*50)
        #     print(f"{self.row_counts=}")
        #     print(f"{self.ranks=}")
        #     print(f"{self.parents=}")

        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            # self.row_counts[src_parent] += self.row_counts[dst_parent]
        else:
            self.parents[src_parent] = dst_parent
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1    

        self.row_counts[dst_parent] += self.row_counts[src_parent]
        self.row_counts[src_parent] = 0
        
        if self.max_row_count < self.row_counts[dst_parent]:
            self.max_row_count = self.row_counts[dst_parent]

        # if verbose:
        #     print(f"{self.row_counts=}")
        #     print(f"{self.ranks=}")
        #     print(f"{self.parents=}")

        return True

    def get_parent(self, table):
        # find parent and compress path
        curr_table = table
        path = []

        while curr_table != self.parents[curr_table]:
            path.append(curr_table)
            curr_table = self.parents[curr_table]
        
        for node in path:
            self.parents[node] = curr_table

        return curr_table
        
def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)

if __name__ == "__main__":
    main()
