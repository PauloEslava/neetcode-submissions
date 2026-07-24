class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        nRows = len(grid)
        nCols = len(grid[0])
        result = 0
        seenSet = set()

        

        def dfs(row, col):
            if col >= nCols or row >= nRows or row < 0 or col < 0 or grid[row][col] == 0 or (row, col) in seenSet:
                return 0
            if grid[row][col] == 1:
                seenSet.add( (row, col) )
                return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    currentArea = dfs(i, j)
                    if currentArea > result:
                        result = currentArea

        return result

        
