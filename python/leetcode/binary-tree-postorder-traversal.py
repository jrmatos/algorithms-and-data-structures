# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.post_order_traverse_node(root, answer)
        return answer
    
    def post_order_traverse_node(self, node, answer):
        if node is None:
            return

        self.post_order_traverse_node(node.left, answer)
        self.post_order_traverse_node(node.right, answer)
        answer.append(node.val)
