# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.pre_order_traverse_node(root, answer)
        return answer

    def pre_order_traverse_node(self, node, answer):
        if node is None:
            return

        answer.append(node.val)
        self.pre_order_traverse_node(node.left, answer)
        self.pre_order_traverse_node(node.right, answer)
