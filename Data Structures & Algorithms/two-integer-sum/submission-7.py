class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Return value is index pair
        # We will ALWAYS find a pair eventually

        diffDict = {}

        for i in range(0, len(nums)):
            if nums[i] in diffDict:
                return [diffDict[nums[i]], i]
            else:
                diffDict[target - nums[i]] = i