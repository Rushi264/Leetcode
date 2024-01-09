# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leaf_checker(root, leaf):
            if not root:
                return 
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            leaf_checker(root.left, leaf)
            leaf_checker(root.right, leaf)

    
        
        leaf1 = []
        leaf2 = []
        leaf_checker(root1, leaf1)
        leaf_checker(root2, leaf2)

        return leaf1 == leaf2

