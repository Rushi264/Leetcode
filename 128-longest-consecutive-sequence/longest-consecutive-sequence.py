class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for n in numSet:
            # we using numSet and not nums beacuse there might be duplicate values in nums and dont want to
            #evaluate those duplicate so to aviod these we can iterate thorough set and actual nums.
            if (n - 1) not in numSet:
                #check if the number is start of the series or not skip it and find the start of the series
                #of numbers.
                y = n
                while y in numSet:
                    y += 1
                maxLen = max(maxLen, y - n)
        return maxLen   



        