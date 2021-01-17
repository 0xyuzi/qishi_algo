"""
input: tree root node 
output: True or false

a valid BST tree node should in the range of [min_val, max_val]
for left tree node, the valid range is [min_val, node.val]
for right tree node, the valid range is [node.val, max_val]

time complexity, O(N) N is the number of nodes in the tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.dfs(root, -sys.maxsize, sys.maxsize)

    def dfs(self, node, min_val, max_val):
        if not node:
            return True
        # check node in the range
        if node.val < min_val or node.val > max_val:
            return False 

        return self.dfs(node.right, node.val, max_val) and self.dfs(node.left, min_val, node.val) 
        