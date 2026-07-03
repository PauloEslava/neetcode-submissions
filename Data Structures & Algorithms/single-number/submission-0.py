class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        repMap = {}

        for num in nums:
            if num not in repMap:
                repMap[num] = 1
            else:
                repMap[num] += 1

        for key in repMap:
            if repMap[key] == 1:
                return key
        