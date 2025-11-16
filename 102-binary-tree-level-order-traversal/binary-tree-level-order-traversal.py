# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        #this is the actual algorithm of bfs as we know bfs travrse through level by level so with some modifiction
        # we can easliy store the levels of our bfs step by step using bfs.
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
