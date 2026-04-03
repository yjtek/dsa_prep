from binarytree import Node
from itertools import permutations
from typing import Optional

def insert(root, key):
    if root is None: 
        return Node(key)
    if key < root.value: 
        root.left = insert(root.left, key)
    else: 
        root.right = insert(root.right, key)
    return root

def build(data):
    root = None
    for x in data: 
        root = insert(root, x)
    print(root, end = ' ')

def buildpermutation(data):
    for d in list(permutations(data)):
        build(d)

class MyNode:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def add_new_node(self, new_node: Node) -> Node:
        empty_left = self.left is None
        empty_right = self.right is None

        if (new_node.value < self.value):
            if (empty_left):
                self.left = new_node
            else: 
                self.left.add_new_node(new_node)
        else:
            if (empty_right):
                self.right = new_node
            else: 
                self.right.add_new_node(new_node)

    def get_height(self):
        empty_left = self.left is None
        empty_right = self.right is None
        if (empty_left and empty_right):
            return 0
        elif (empty_left):
            return 1 + self.right.get_height()
        elif (empty_right):
            return 1 + self.left.get_height()
        else:
            return 1 + max(self.left.get_height(), self.right.get_height())
        
    def get_balance_factor(self):
        if self.get_height() == 0:
            return 0
        
        left_height = 0 if self.left is None else self.left.get_height() + 1
        right_height = 0 if self.right is None else self.right.get_height() + 1

        return left_height - right_height
    
    def is_imbalanced(self):
        return self.get_balance_factor() not in [-1, 0, 1]

    def display(self, level=0, prefix="Root: ") -> None:
        if self.right:
            self.right.display(level + 1, "R: ")
        print("    " * level + prefix + str(self.value))
        if self.left:
            self.left.display(level + 1, "L: ")


def ll_rotation(root: MyNode):
    new_root = root.left
    new_root.right = root
    root.left = None
    return new_root

def rr_rotation(root: MyNode):
    new_root = root.right
    new_root.left = root
    root.right = None
    return new_root

def lr_rotation(root: MyNode) -> MyNode:
    new_root = root.left.right
    new_root.left = root.left
    new_root.right = root
    root.left.right = None
    root.left = None
    return new_root

def rl_rotation(root: MyNode) -> MyNode:
    # 1. Identify the three key players
    old_root_right = root.right      # The right child (30)
    old_root_right_left = old_root_right.left          # The left-grandchild (25) - Our NEW root

    # 2. Save x's children (the "orphans")
    old_root_right_left_left = old_root_right_left.left         # Values between 20 and 25 (like 22)
    old_root_right_left_right = old_root_right_left.right        # Values between 25 and 30 (none in your example)

    # 3. Perform the "Pivots"
    old_root_right_left.left = root          # 20 becomes 25's left
    old_root_right_left.right = old_root_right         # 30 becomes 25's right

    # 4. Hand off the orphans to the new parents
    root.right = old_root_right_left_left        # 22 is > 20, so it goes to 20's right
    old_root_right.left = old_root_right_left_right         # Anything in t3 is < 30, so it goes to 30's left

    return old_root_right_left # new root
