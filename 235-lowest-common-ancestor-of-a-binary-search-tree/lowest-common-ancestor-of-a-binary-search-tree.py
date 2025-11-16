# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            #if both node is in less than node we are on we can say that both nodes exist in left
            #since this is bst.
            elif p.val > curr.val and q.val > curr.val:
            #we can say the same for this of both of them are greater than the node we are on, then
            # we move right
                curr = curr.right
            else:
                return curr
            #for the remaining condition our result nodes are either spliting or one of them is
            #is matching our current node we are on so which means we can return our current node.
        