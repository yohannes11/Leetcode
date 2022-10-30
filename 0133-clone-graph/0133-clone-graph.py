"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        copied = {}
        def copy_node(current_node):
            if current_node.val in copied:
                return copied[current_node.val]
            new_node = Node(current_node.val)
            copied[current_node.val] = new_node
            neighbors = []
            for node_neighbour in current_node.neighbors:
                new_neighbour = copy_node(node_neighbour)
                neighbors.append(new_neighbour)
            new_node.neighbors = neighbors.copy()
            return new_node
        return copy_node(node)
                
                    
                
        