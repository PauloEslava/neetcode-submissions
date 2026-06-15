# 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultList = []
        suffixes = []
        prefixes = []

        for i in range(len(nums)):
            multiplication_stacker = 1

            for value in nums[0:i]:
                multiplication_stacker = multiplication_stacker * value
            suffixes.append(multiplication_stacker)

            multiplication_stacker = 1

            for value in nums[i+1:]:
                multiplication_stacker = multiplication_stacker * value
            prefixes.append(multiplication_stacker)

        resultList = []
        for i in range(len(nums)):
            resultList.append(prefixes[i] * suffixes[i])

        return resultList


                



        