# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # res[0] will hold the global maximum path sum found anywhere in the tree
        # We use a list so it can be modified inside the dfs function
        res = [root.val]

        def dfs(root):
            # Base case: if we hit a null node, it contributes 0 to a path
            if not root:
                return 0

            # Recursively compute max path sums from left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If a subtree contributes a negative value, it's better to not include it at all
            # So we clamp both to a minimum of 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Now compute the **maximum path sum passing THROUGH this root**
            # This includes the node itself + best left path + best right path
            # This is a "full split" path (left → root → right)
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # For returning upward: we can only return ONE SIDE (not both),
            # because when going up to parent we must keep the path single-directional.
            # So return root value + best of left/right
            return root.val + max(leftMax, rightMax)

        # Run DFS to compute max path sum
        dfs(root)

        # Return the global maximum path sum found
        return res[0]
