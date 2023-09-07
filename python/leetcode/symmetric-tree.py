# https://leetcode.com/problems/symmetric-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.BFS(root)

    def BFS(self, root):
        if root.left is None and root.right is None:
            return True

        queue_left = deque()
        queue_right = deque()

        queue_left.append(root.left)
        queue_right.append(root.right)

        while queue_left and queue_right:
            node_left = queue_left.popleft()
            node_right = queue_right.popleft()

            if not node_left and not node_right:
                continue

            if node_left is None and node_right is not None:
                return False

            if node_right is None and node_left is not None:
                return False

            if node_left and node_right and node_left.val != node_right.val:
                return False

            if node_left:
                queue_left.append(node_left.left)
                queue_left.append(node_left.right)

            if node_right:
                queue_right.append(node_right.right)
                queue_right.append(node_right.left)

        return True