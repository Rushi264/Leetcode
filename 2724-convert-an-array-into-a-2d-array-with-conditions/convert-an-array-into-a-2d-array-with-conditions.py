class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        while hashmap:
            temp_list = []
            
            for key in list(hashmap.keys()):
                if hashmap[key] > 0:
                    temp_list.append(key)
                    hashmap[key] -= 1
                
                if hashmap[key] == 0:
                    del hashmap[key]
            
            result.append(temp_list)
        
        return result
                

