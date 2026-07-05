class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # Set of tuples pairing (row, column)
        nIslands = 0
        nRows = len(grid)
        nCols = len(grid[0])

        # When we find a 1, we mark all other adjacent ones as visited so we count em as a big island
        def dfs(row, col):
            if((row, col) in visited or row >= nRows or col >= nCols or row < 0 or col < 0 or grid[row][col] == "0"):
                return 0
            else:
                 visited.add((row, col))
                 return dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)


        for row in range(0, nRows):
            for col in range(0, nCols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    nIslands += 1

        return nIslands

