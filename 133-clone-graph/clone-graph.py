"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # Hash map to store the mapping:
        # original_node -> cloned_node
        oldToNew = {}

        def dfs(node):
            """
            Returns a deep copy of the given node using DFS.
            Ensures that each original node is cloned only once,
            preventing infinite recursion in cycles.
            """

            # If this node is already cloned, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # Create a copy with the same value, empty neighbors for now
            copy = Node(node.val)
            
            # Store the clone in the hashmap before exploring neighbors
            # This prevents infinite recursion in cyclic graphs
            oldToNew[node] = copy

            # Recursively clone all neighbors and add them to the clone
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        # If input graph is empty, return None
        return dfs(node) if node else None
