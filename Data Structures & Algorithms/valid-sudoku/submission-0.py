class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First we check all rows
        for i in range(9):
            seen_checklist = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif seen_checklist[board[i][j]] == True:
                    return False
                else:
                    seen_checklist[board[i][j]] = True

        print(seen_checklist)

        #Then we check all columns
        for i in range(9):
            seen_checklist = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif seen_checklist[board[j][i]] == True:
                    return False
                else:
                    seen_checklist[board[j][i]] = True
        
        #Then we check all 9 3x3 squares
        for i in range(3):
            for j in range(3):
                seen_checklist = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False}
                
                # Now iterate through the 9 cells in THIS 3x3 square
                for row in range(3):
                    for col in range(3):
                        actual_row = i * 3 + row  # Convert square position to board row
                        actual_col = j * 3 + col  # Convert square position to board col
                        
                        if board[actual_row][actual_col] == ".":
                            continue
                        elif seen_checklist[board[actual_row][actual_col]] == True:
                            return False
                        else:
                            seen_checklist[board[actual_row][actual_col]] = True



        return True
            

        