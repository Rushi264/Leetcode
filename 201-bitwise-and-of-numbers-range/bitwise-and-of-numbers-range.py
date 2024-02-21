class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        # Find the common prefix bits
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        # Append zeros to the right
        return left << shift