class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            count += 1
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x, 0) + 1

        max_key = max(hashmap, key = hashmap.get)
        return max_key
        