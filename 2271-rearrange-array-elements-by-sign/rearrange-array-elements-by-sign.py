class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        array1 = []
        array2 = []
        index = 0
        for i in nums:
            if i > 0:
                array1.append(i)
            else:
                array2.append(i)
        for x in range(len(array1)):
            nums[index] = array1[x]
            index += 1
            nums[index] = array2[x]
            index += 1

        return nums

