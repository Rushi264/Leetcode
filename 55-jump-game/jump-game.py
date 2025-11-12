class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
            #try to take an example and understand this then it would be logical of why we  
            # are doing this
                goal = i
        return True if goal == 0 else False

        