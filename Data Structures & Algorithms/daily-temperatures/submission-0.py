class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # To have 0 if there isnt a warmer day, we simply assume the base case to be that.
        results = [0] * len(temperatures)
        tempStack = []

        # We will be evaluating temperature - index pairs
        for i in range(0, len(temperatures)):
            print("tempStack")
            print(tempStack)

            if tempStack:
                while tempStack and temperatures[i] > tempStack[-1][0]:
                    # We pop the top and update the days passed in results
                    results[tempStack[-1][1]] = i - tempStack[-1][1]
                    tempStack.pop()

            # As long as the top of the stack is smaller than today's temp
            tempStack.append([temperatures[i], i])

        return results


        