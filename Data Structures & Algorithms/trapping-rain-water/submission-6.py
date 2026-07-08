class Solution:
    def trap(self, height: List[int]) -> int:
        leftSet = []
        rightSet = []
        water = 0
        currentMax = 0

        for bar in height:
            if bar > currentMax:
                currentMax = bar
            leftSet.append(currentMax)

        currentMax = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > currentMax:
                currentMax = height[i]
            rightSet.append(currentMax)
        rightSet.reverse()

        for i in range(len(height)):
            currentWater = min(rightSet[i], leftSet[i]) - height[i]
            if currentWater < 0:
                currentWater = 0
            water += currentWater

        print(leftSet)
        print(rightSet)
        return water
