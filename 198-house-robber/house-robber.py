class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        rob1, rob2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp

        return rob2