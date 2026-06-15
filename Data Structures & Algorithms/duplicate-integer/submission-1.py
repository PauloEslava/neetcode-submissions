class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for item in nums:
            amount = nums.count(item) 
            if amount > 1:
                return True

        return False
        