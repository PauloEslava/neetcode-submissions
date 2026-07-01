class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        longest = 0
        length = 1
        for num in nums:
            numSet.add(num)

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

            



        