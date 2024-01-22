# python3

import sys
import threading

# from dataclasses import dataclass, field
# from typing import Type

# @dataclass
class Node:
    def __init__(self, index, parent=[], child=[]):
        self.index = index
        self.parent = parent
        self.child = child
    
    def __repr__(self):
        return f"Node({self.index=}, {self.parent=}, {self.child=})"

def build_tree(parents):
    all_nodes = [Node(index=index, parent=[], child=[]) for index in range(len(parents))]

    for index in range(len(all_nodes)):        
        if parents[index] == -1:
            root = all_nodes[index]
            all_nodes[index].parent = None
        else:
            all_nodes[index].parent = all_nodes[parents[index]]
            all_nodes[index].parent.child.append(all_nodes[index])
                
    #return root, all_nodes
    return root

def compute_height(root):    
    if root.child == []:
        return 1
    max_height = 0
    for child in root.child:
        subtree_root = child
        subtree_height = compute_height(subtree_root)
        max_height = max(
            max_height, 
            subtree_height+1
        )
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    root = build_tree(parents)
    print(compute_height(root))


if  __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**25)   # new thread will get stack of such size
    threading.Thread(target=main).start()
    

