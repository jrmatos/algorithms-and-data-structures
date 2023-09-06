# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.BFS(cloned, target)

    def BFS(self, node, target):
        queue = deque()
        queue.append(node)

        while queue:
            curr_node = queue.popleft()

            if curr_node is not None:
                if curr_node.val == target.val:
                    return curr_node

                queue.append(curr_node.left)
                queue.append(curr_node.right)

        return None
