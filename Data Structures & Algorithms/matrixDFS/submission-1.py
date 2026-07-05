class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited  = set()
        paths = 0
        nRows = len(grid)
        nCols = len(grid[0])

        def dfs(row, col):
            if row >= nRows or col >= nCols or row < 0 or col < 0 or grid[row][col] == 1 or (row, col) in visited:
                return 0
            if row == nRows - 1  and col == nCols - 1:
                return 1
            else:
                visited.add((row, col))
                result = dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
                visited.remove((row, col))
                return result

        return dfs(0, 0)
        