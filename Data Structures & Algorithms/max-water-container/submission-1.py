class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bigWater = 0
        left = 0
        right = len(heights) - 1

        while True:
            if left > right:
                return bigWater
            
            currentWater = ( min(heights[left], heights[right]) * (right - left))
            if currentWater > bigWater:
                bigWater = currentWater

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1