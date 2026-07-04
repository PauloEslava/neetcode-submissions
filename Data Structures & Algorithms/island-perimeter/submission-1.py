class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        perimeter = 0
        nRows = len(grid)
        nCols = len(grid[0])

        def depthFirstSearch(row, col):
            if (row >= nRows or col >= nCols or row < 0 or col < 0 or grid[row][col] == 0):
                return 1
            elif (row, col) in visited:
                return 0
            else:
                visited.add((row, col))
                return depthFirstSearch(row + 1, col) + depthFirstSearch(row - 1, col) + depthFirstSearch(row, col + 1) + depthFirstSearch(row, col - 1)

        for r in range(0, nRows):
            for c in range(0, nCols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return depthFirstSearch(r, c)
