class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = -1
        left = 0

        while True:
            sumTarget = numbers[left] + numbers[right]

            if sumTarget == target:
                return [left + 1, len(numbers) + right + 1]

            elif sumTarget > target:
                right = right - 1

            elif sumTarget < target:
                left = left + 1




        