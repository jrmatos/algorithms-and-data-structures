# https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.BFS(p, q)

    def BFS(self, node_p, node_q):
        queue_p = deque()
        queue_q = deque()

        queue_p.append(node_p)
        queue_q.append(node_q)

        while queue_p and queue_q:
            curr_p = queue_p.popleft()
            curr_q = queue_q.popleft()

            if curr_p is None and curr_q is not None:
                return False

            if curr_q is None and curr_p is not None:
                return False

            if curr_p and curr_q and curr_p.val != curr_q.val:
                return False

            if curr_p:
                queue_p.append(curr_p.left)
                queue_p.append(curr_p.right)

            if curr_q:
                queue_q.append(curr_q.left)
                queue_q.append(curr_q.right)
            
        return True