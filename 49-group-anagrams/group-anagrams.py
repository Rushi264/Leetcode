from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Sort the characters in the string and use it as a key
            sorted_s = ''.join(sorted(s))
            
            # Append the original string to the list of anagrams with the same key
            anagrams[sorted_s].append(s)
        
        # Convert the values of the dictionary to a list to get the grouped anagrams
        grouped_anagrams = list(anagrams.values())
        
        return grouped_anagrams