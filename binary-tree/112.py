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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            curr_root, target = stack.pop()

            if not curr_root:
                continue

            if not curr_root.right and not curr_root.left and target == curr_root.val:
                return True

            if curr_root.right:
                stack.append((curr_root.right, target - curr_root.val))
            if curr_root.left:
                stack.append((curr_root.left, target - curr_root.val))

        return False


print(
    Solution().hasPathSum2(
        array_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22
    )
)

print(Solution().hasPathSum2(array_to_tree([1, 2, 3]), 5))
print(Solution().hasPathSum2(array_to_tree([]), 0))
print(Solution().hasPathSum2(array_to_tree([1, 2]), 1))
print(Solution().hasPathSum2(array_to_tree([1]), 1))
