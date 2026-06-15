class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = []
        dupeStatus = False
        for number in nums:
            if number in seenNums:
                dupeStatus = True     
            if number not in seenNums:
                seenNums.append(number)
        return dupeStatus


        