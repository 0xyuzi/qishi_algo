# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None 
        
        root = TreeNode(preorder[0])
    
        
        # find the boundary of index in inorder list to build this left subtree
        for index, pre_val in enumerate(inorder):
            if pre_val == preorder[0]:
                break
        
        # recursive call to build left subtree
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        
        
        
        # then go to the build the right subtree
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return root