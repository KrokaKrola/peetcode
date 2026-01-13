from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            if not node:
                continue

            result = max(result, depth)
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

        return result

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth2(root.left)
        right = self.maxDepth2(root.right)

        return max(left, right) + 1
