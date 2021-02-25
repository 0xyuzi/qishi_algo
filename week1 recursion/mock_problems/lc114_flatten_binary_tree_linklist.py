# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return None 
        
        
        left = self.flatten(root.left) if root.left else None 
        right = self.flatten(root.right) if root.right else None 
        
        if left:
            node = left 
            # find the rightest node of the left substree
            while node.right:
                node = node.right
            
            root.right = root.left
            
            node.right = right
            root.left = None 
            
        else:
            root.right = right
        
        return root 
            