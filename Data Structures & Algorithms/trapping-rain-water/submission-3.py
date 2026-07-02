class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        water = 0
        currentMax = 0

        for bar in height:
            if bar > currentMax:
                currentMax = bar
            leftMax.append(currentMax)

        currentMax = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > currentMax:
                currentMax = height[i]
            rightMax.append(currentMax)
        rightMax.reverse()

        for i in range(0, len(height)):
            currentWater = min(leftMax[i], rightMax[i]) - height[i]
            if currentWater > 0:
                water += currentWater

        return(water)