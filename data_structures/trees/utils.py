from binarytree import Node
from itertools import permutations
from typing import Optional
from collections import deque
from abc import ABC, abstractmethod

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

class BaseNode(ABC):
    def __init__(self, value: int, left: Optional[BaseNode] = None, right: Optional[BaseNode] = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"""{self.__class__.__name__}({self.value}, left={self.left.value if self.left else None}, right={self.right.value if self.right else None})"""

    @abstractmethod
    def add_new_node(self, value: int) -> BaseNode:
        """Each subclass must implement its own insertion/balancing logic."""
        pass

    def get_height(self) -> int:
        l_height = self.left.get_height() + 1 if self.left else 0
        r_height = self.right.get_height() + 1 if self.right else 0
        return max(l_height, r_height)

    def get_balance_factor(self) -> int:
        l_h = self.left.get_height() + 1 if self.left else 0
        r_h = self.right.get_height() + 1 if self.right else 0
        return l_h - r_h

    def is_imbalanced(self):
        return self.get_balance_factor() not in [-1, 0, 1]
    
    def display(self, level=0, prefix="Root: ") -> None:
        if self.right:
            self.right.display(level + 1, "R: ")
        print("    " * level + prefix + str(self.value))
        if self.left:
            self.left.display(level + 1, "L: ")

class MyNode(BaseNode):
    def add_new_node(self, value: int) -> MyNode:
        if value < self.value:
            if not self.left: 
                self.left = MyNode(value)
            else: 
                self.left.add_new_node(value)
        elif value > self.value:
            if not self.right: 
                self.right = MyNode(value)
            else: 
                self.right.add_new_node(value)
        else:
            raise ValueError("Duplicate values not allowed in BST")
        
        return self
        
class MyAVLNode(BaseNode):
    def add_new_node(self, value: int) -> MyAVLNode:
        if value < self.value:
            if not self.left: 
                self.left = MyAVLNode(value)
            else: 
                self.left = self.left.add_new_node(value)
        elif value > self.value:
            if not self.right: 
                self.right = MyAVLNode(value)
            else: 
                self.right = self.right.add_new_node(value)
        else:
            raise ValueError("Duplicate values not allowed")

        bf = self.get_balance_factor()

        if bf > 1: # Left Heavy
            if value < self.left.value: # LL Case
                return self._rotate_right()
            else: # LR Case
                self.left = self.left._rotate_left()
                return self._rotate_right()
        
        if bf < -1: # Right Heavy
            if value > self.right.value: # RR Case
                return self._rotate_left()
            else: # RL Case
                self.right = self.right._rotate_right()
                return self._rotate_left()

        return self

    def _rotate_right(self) -> MyAVLNode:
        new_root = self.left
        handoff = new_root.right
        
        new_root.right = self
        self.left = handoff
        return new_root

    def _rotate_left(self) -> MyAVLNode:
        new_root = self.right
        handoff = new_root.left
        
        new_root.left = self
        self.right = handoff
        return new_root


def display_visual(root: MyNode):
    if not root:
        return

    # Helper to get tree depth for spacing
    def get_height(node):
        if not node: return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    height = get_height(root)
    queue = deque([(root, 0, 0, 2**(height-1))]) # node, level, column, offset
    
    levels = {}
    
    while queue:
        node, level, col, offset = queue.popleft()
        if level not in levels:
            levels[level] = []
        levels[level].append((node.value, col))
        
        if node.left:
            queue.append((node.left, level + 1, col - offset//2, offset//2))
        if node.right:
            queue.append((node.right, level + 1, col + offset//2, offset//2))

    # Print the levels
    for i in range(height):
        line = [" "] * (2**height * 2)
        for val, col in levels[i]:
            line[2**(height-1) + col] = str(val)
        print("".join(line))

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
