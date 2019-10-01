# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total_sum = 0
        if not root:
            return total_sum
        stack = [root]
        while stack:
            node = stack.pop()
			# check node value is exist.
            if not node.val:
                continue
            if L <= node.val <= R:
                total_sum += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            elif node.val < L and node.right:
                stack.append(node.right)
            elif node.val > R and node.left:
                stack.append(node.left)
        return total_sum