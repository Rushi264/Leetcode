class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        array1 = []
        array2 = []
        final = []
        i,j = 0,0
        for i in nums:
            if i > 0:
                array1.append(i)
            else:
                array2.append(i)
        for x in range(len(array1)):
            final.append(array1[x])
            final.append(array2[x])

        return final

