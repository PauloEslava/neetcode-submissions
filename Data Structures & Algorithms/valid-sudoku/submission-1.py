class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

    # We need to check rows, columns and 9x9s

        seenSet = set()
        
        for row in board: # We verify rows
            seenSet = set()
            for num in row:
                if num == ".":
                    continue
                if num not in seenSet:
                    seenSet.add(num)
                else:
                    return False
        
        for i in range (0,9): # We verify columns
            seenSet = set()
            for j in range (0, 9):
                num = board[j][i]
                if num == ".":
                    continue
                if num not in seenSet:
                    seenSet.add(num)
                else:
                    return False

        # Now we check for the sub 3x3s. We basically we check a big 3x3 made of 3x3s
        for iBig in range(0,9,3):
            for jBig in range(0,9,3):
                seenSet = set()
                for i in range(0,3):
                    for j in range(0,3):
                        num = board[j + jBig][i + iBig] # We add the big is and js to correct offset
                        if num == ".":
                            continue
                        if num not in seenSet:
                            seenSet.add(num)
                        else:
                            return False




        return True