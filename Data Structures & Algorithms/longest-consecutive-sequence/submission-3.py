class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        longest = 0
        length = 1
        for num in nums:
            numSet.add(num)

        for num in numSet:
            # We know we are at the start of a sequence if num - 1 doesnt exist
            if (num - 1) not in numSet: 
                length = 1
                # As long as the sequence continues, length grows
                while num + length in numSet:
                    length += 1
                # For every sequence started at number num, we check if its the longest
                longest = max(longest, length)

        # Return the absolute longest
        return longest

            



        