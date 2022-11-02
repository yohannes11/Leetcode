# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result_array = []
        visited = set()
        def inorder_traversal(node,result_array):
            queue = [node]
            current_node = node
            while current_node.left:
                queue.append(current_node.left)
                current_node = current_node.left
            while queue:    
                current_node = queue.pop()
                result_array.append(current_node.val)
                if current_node.right:
                    inorder_traversal(current_node.right,result_array)
                else:
                    pass
        inorder_traversal(root,result_array)
        return result_array[k-1]
                
                        
            
        
    '''
        5
       / \
      3   6
     /  \   
    2    4
   /    
  1 
   \
    9
   / \
  9   9
  '''