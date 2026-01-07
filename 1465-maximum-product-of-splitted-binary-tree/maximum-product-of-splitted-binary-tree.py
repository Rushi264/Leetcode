# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        def evaluate_sum(node):
            if not node:
                return 0

            total_sum = node.val + evaluate_sum(node.left) + evaluate_sum(node.right)

            return total_sum
        
        total = evaluate_sum(root)
        best = 0
        def subtree_sum(node):
            nonlocal best
            if not node:
                return 0

            left = subtree_sum(node.left)
            right = subtree_sum(node.right)
            s =  node.val + left + right
            best = max(best, s*(total - s))

            return s

        subtree_sum(root)

        return best % MOD


        