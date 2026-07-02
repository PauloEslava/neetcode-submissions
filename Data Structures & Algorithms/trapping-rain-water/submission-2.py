class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxes = []
        rightMaxes = []
        water = 0
        currentMax = 0

        for i in range(0, len(height)):
            if height[i] > currentMax:
                currentMax = height[i]
            leftMaxes.append(currentMax)

        currentMax = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > currentMax:
                currentMax = height[i]
            rightMaxes.append(currentMax)
        rightMaxes.reverse()

        for i in range(0, len(leftMaxes)):
            waterAtPos = min(leftMaxes[i], rightMaxes[i]) - height[i]

            if waterAtPos < 0:
                water += 0
            else:
                water += waterAtPos

        print(rightMaxes, leftMaxes)
        return water