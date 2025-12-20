class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        
        for n in nums:
           
            hashmap[n] = hashmap.get(n, 0) + 1
        
        hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        return [n for n, i in hashmap[:k]]
        