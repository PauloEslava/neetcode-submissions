class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        currentIndex = 0
        for num in nums:
            if num in diffMap:
                return [diffMap[num], currentIndex]
            else:
                diffMap[target-num] = currentIndex
                currentIndex += 1
        
        