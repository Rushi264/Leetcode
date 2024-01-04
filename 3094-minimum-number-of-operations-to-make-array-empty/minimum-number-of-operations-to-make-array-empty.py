class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = 0
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key in list(hashmap.keys()):
            value = math.ceil(hashmap[key] / 3)

            if hashmap[key] <= 1:
                return -1
            if hashmap[key] == 2 or hashmap[key] == 3:
                count = count + 1
            else:
                count = count + value
        return count
        




        
