class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = -1
        left = 0

        while True:

            if numbers[left] + numbers[right] == target:
                return [left + 1, len(numbers) + right + 1]

            elif numbers[left] + numbers[right] > target:
                right = right - 1

            elif numbers[left] + numbers[right] < target:
                left = left + 1




        