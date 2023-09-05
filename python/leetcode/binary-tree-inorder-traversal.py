# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.in_order_traverse_node(root, answer)
        return answer

    def in_order_traverse_node(self, node, answer):
        if node is None:
            return

        self.in_order_traverse_node(node.left, answer)
        answer.append(node.val)
        self.in_order_traverse_node(node.right, answer)
