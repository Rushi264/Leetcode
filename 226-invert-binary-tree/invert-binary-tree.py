# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        #swap the places of child nodes.

        self.invertTree(root.left)
        self.invertTree(root.right)
        #reccuse through left side and right side of the tree to swap all the childens as well.

        return root