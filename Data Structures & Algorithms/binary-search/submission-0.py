class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch (left, right, array, target):
            mid = (right + left)//2

            if left > right:
                return -1

            if target == array[mid]:
                return mid

            if target > array[mid]:
                return binarySearch(mid + 1, right, array, target)

            if target < array[mid]:
                return binarySearch(left, mid - 1, array, target)


        return binarySearch(0, len(nums) - 1, nums, target)


        