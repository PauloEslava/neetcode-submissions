class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxes = []
        rightMaxes = []
        water = 0
        currentMax = 0
        
        for bar in height:
            if bar > currentMax:
                currentMax = bar
            leftMaxes.append(currentMax)

        currentMax = 0

        for pos in range(len(height) - 1, -1, -1):
            if height[pos] > currentMax:
                currentMax = height[pos]
            rightMaxes.append(currentMax)
        rightMaxes.reverse()

        for i in range (len(height)):
            currentWater = min(leftMaxes[i], rightMaxes[i]) - height[i]
            if currentWater > 0:
                water += currentWater
        
        return water
