class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        bigWater = 0
        done = False

        while done != True:
            currentWater = min(heights[left], heights[right]) * (right - left)
            if currentWater > bigWater:
                bigWater = currentWater

            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1

            if left == right:
                return bigWater