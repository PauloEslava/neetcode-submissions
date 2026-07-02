class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0

        for i in range(0, len(height)):
            rightMax = max(height[i : len(height) ] )
            leftMax = max(height [ 0 : i + 1 ] )
            currentWater = min(rightMax,leftMax) - height[i]
            if currentWater < 0:
                currentWater = 0


            totalWater += currentWater

        
        return totalWater