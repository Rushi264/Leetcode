class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))    
        
    def helper(self,nums):    
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(rob1 + n,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    #this is a similar problem to House Robber I, there is slight change in it that we cannot rob the exretme right
    # and Extreme left at the same time, so we just build our logic in helper function and passed two array each 
    # so we checked what if we icnlude left value and what if we include right value, with this we can evaluate which 
    # should be considered in our solution by getting max of those two array and if there is only one value in an 
    # array then we wll need to return just value so that why we icnluded that as well in our max function.
        