class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffDict = {}
        for num in numbers:
            if num in diffDict:
                return [numbers.index(diffDict[num]) + 1, numbers.index(num) + 1]
            else:
                diffDict[target - num] = num



        