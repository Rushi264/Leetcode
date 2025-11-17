# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # If either preorder or inorder is empty, no tree can be built → return None
        if not preorder or not inorder:
            return None

        # The first element of preorder is ALWAYS the root of the current subtree
        root = TreeNode(preorder[0])

        # Find where this root appears in the inorder list
        # Everything left of this index is the left subtree
        # Everything right of this index is the right subtree
        mid = inorder.index(preorder[0])

        # Construct the left subtree:
        # preorder[1 : mid+1] → skip root and take next 'mid' elements for the left subtree
        # inorder[:mid] → all nodes before the root in inorder belong to the left subtree
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # Construct the right subtree:
        # preorder[mid+1 : ] → remaining preorder elements belong to right subtree
        # inorder[mid+1 : ] → all nodes after the root in inorder belong to the right subtree
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        # Return the constructed tree root for this subtree
        return root
