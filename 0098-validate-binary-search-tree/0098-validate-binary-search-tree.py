# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
         7
     5       10
    4  6    9   12
  3



'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return
        def check_sub_tree(node, min_bound, max_bound):
            if node is None: return True
            if node.val >= max_bound or node.val<= min_bound: return False
            return check_sub_tree(node.left,min_bound,node.val) and check_sub_tree(node.right,node.val,max_bound) 
        return check_sub_tree(root,float('-inf'),float('inf')) 
        
        
            
        
        
            
            
        
        
        
        
                
    