# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        return self.DFS(root, max_depth)

    def DFS(self, node, max_depth):
        if node is None:
            return max_depth

        max_depth += 1
        
        left_max_depth = self.DFS(node.left, max_depth)
        right_max_depth = self.DFS(node.right, max_depth)

        return max(left_max_depth, right_max_depth)