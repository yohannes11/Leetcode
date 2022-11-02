# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder_traversal(node,output_array):
            if node is None: return output_array
            inorder_traversal(node.left,output_array)
            if node is not None:
                output_array.append(node.val)
            inorder_traversal(node.right,output_array)
            return output_array
            
        output_array = inorder_traversal(root,[])
        return output_array[k-1]
        
            