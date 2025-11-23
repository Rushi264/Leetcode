class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        present = set()

        for i in nums:
            if i in present:
                return True
            present.add(i)
        return False
        