"""
input: root of a binary tree
output: root of the linked list in-place
linked-list: linked to the right node

transverse order: node->left->right


"""
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
            return None, None
        
        right = root.right 
        

        root.right, end_left_node = self.flatten(root.left)
        
        root.left = None 
        
        if end_left_node:
            end_left_node.right, end_right_node = self.flatten(right)
        else:
            return root, root

        
            
#         if not end_right_node:
#             return root, root
        
        return root, end_right_node 
        