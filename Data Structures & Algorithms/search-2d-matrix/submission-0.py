class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch (left, right, array, target):
            mid = (right + left)//2

            if left > right:
                return -1

            if target == array[mid]:
                return target

            if target > array[mid]:
                return binarySearch(mid + 1, right, array, target)

            if target < array[mid]:
                return binarySearch(left, mid - 1, array, target)

        for row in matrix:
            result = binarySearch(0, len(row) - 1, row, target)
            if result == -1:
                continue
            if result == target:
                return True
        return False