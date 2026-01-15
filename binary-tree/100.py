# Definition for a binary tree node.
from collections import deque
from typing import Optional


def array_to_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        curr = queue.popleft()

        # Process left child
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1

        # Process right child
        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1

    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return self.isSame(p, q)

    def isSame(
        self, left_root: Optional[TreeNode], right_root: Optional[TreeNode]
    ) -> bool:
        if left_root is None and right_root is None:
            return True

        if left_root is None or right_root is None:
            return False

        if left_root.val != right_root.val:
            return False

        return self.isSame(left_root.left, right_root.left) and self.isSame(
            left_root.right, right_root.right
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        stack = [(p, q)]

        while stack:
            left_root, right_root = stack.pop()

            if not left_root and not right_root:
                continue

            if not left_root or not right_root:
                return False

            if left_root.val != right_root.val:
                return False

            stack.append((left_root.left, right_root.left))
            stack.append((left_root.right, right_root.right))

        return True
