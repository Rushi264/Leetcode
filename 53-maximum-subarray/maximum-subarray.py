class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Start both with the first element to handle all-negative arrays
        best = nums[0]          # best (global max so far)
        curr = nums[0]          # curr (best subarray sum ending at current index)
        
        # Walk through the rest of the array
        for k in range(1, len(nums)):
            x = nums[k]
            # Either extend the previous subarray or start fresh at x
            curr = max(x, curr + x)
            # Update the global best
            best = max(best, curr)
        
        return best