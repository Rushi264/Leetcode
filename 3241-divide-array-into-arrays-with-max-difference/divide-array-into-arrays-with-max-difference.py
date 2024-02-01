class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums = sorted(nums)
        final = []
        subarray = []

        for i in range(0, len(nums), 3):
            subarray = nums[i:i+3]  # Extract subarray of length 3
            final.append(subarray)
        for i in final:
            if i[2] - i[0] > k:
                return []
        return final
                


        