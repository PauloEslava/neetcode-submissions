class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # First, we will have to go through the entire array
        for i in range(len(arr)):

            # If we haven't reached the end, we go ahead with the replacement
            if i < len(arr) - 1:
                # We turn the current number into its right neighbor, this ensures the maximum number in the array doesn't remain unchanged
                arr[i]  = arr[i + 1]

                # We check the whole array so that the current position's value will be replaced for the absolute largest number to its right
                for j in range (i + 1 , len(arr)):
                    if arr[j] > arr[i]:
                         arr[i] = arr[j]

            # If we reach the end, we save the entire replacement and just equal it to -1
            elif i == len(arr) - 1:
                arr[i] = -1

        return arr


# We replace the number to the one on its right because:
# 1. If we are to to keep it as it is, the largest values in the list never get replaced (nothing is larger than then)
# 2. This way, best case the one next to them is the largest and worst case we just go through the whole array