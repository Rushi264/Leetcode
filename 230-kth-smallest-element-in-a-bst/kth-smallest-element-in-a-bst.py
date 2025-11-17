# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        n = 0              # counter to track how many nodes we've visited in sorted (in-order) order
        stack = []         # stack to simulate recursion for in-order traversal
        curr = root        # start traversal from the root node

        # continue while there is a current node to go down from
        # OR while there are nodes on the stack that we still need to process
        while curr or stack:

            # go as far left as possible from the current node
            # (left subtree of a BST contains smaller values)
            while curr:
                stack.append(curr)   # push current node onto the stack to come back to it later
                curr = curr.left     # move to the left child

            # when there is no more left child, we process the node on top of the stack
            curr = stack.pop()       # this is the next smallest node in the BST

            n += 1                   # we've now visited one more node in in-order sequence

            if n == k:               # if this is the k-th visited node
                return curr.val      # its value is the k-th smallest, so return it

            # after visiting the current node, move to its right subtree
            curr = curr.right        # next iteration will again go left from here (if not None)
