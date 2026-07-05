class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        foundCoords = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    foundCoords.append([i, j])

        for pair in foundCoords:
            for i in range(0, len(matrix)):
                matrix[i][pair[1]] = 0
            for j in range(0, len(matrix[0])):
                matrix[pair[0]][j] = 0