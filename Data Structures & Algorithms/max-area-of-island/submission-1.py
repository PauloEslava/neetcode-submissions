class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        nRows = len(grid)
        nCols = len(grid[0])

        def depthFirstSearch(row, col):
            if (row >= nRows or col >= nCols or row < 0 or col < 0 or grid[row][col] == 0 or (row, col) in visited):# TODO: Check all base cases
                return 0
            else:
                visited.add((row, col))
                return 1 + depthFirstSearch(row + 1, col) + depthFirstSearch(row - 1, col) + depthFirstSearch(row, col + 1) + depthFirstSearch(row, col - 1)

        for r in range(0, nRows):
            for c in range(0, nCols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currentArea = depthFirstSearch(r, c)
                    maxArea = max(maxArea, currentArea)

        return maxArea

