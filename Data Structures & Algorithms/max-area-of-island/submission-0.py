class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set() # The visited parts will be stored as coordinate pairs
        nRows = len(grid)
        nCols = len(grid[0])
        maxArea = 0

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= nRows or col >= nCols or (row, col) in visited or grid[row][col] == 0):
                return 0
            else:
                visited.add((row, col))
                return 1 + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row - 1, col) + dfs(row, col - 1)

        for r in range(0, nRows):
            for c in range(0, nCols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
        print(maxArea)

        return maxArea
        