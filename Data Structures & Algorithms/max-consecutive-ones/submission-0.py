class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        highScore = 0

        for num in nums:
            if num == 1:
                counter = counter + 1

            if counter > highScore:
                highScore = counter

            elif num == 0:
                counter = 0

        return highScore

        