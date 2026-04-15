def isvalidsudoku(board: list[list[str]]) -> bool:
    for row in board:
        nums_str = []
        for num in row:
            if num !=".":
                if num in nums_str: 
                    return False
                else:
                    nums_str.append(num)

    for place in range(9):
        nums_col = []
        for row in board:
            if row[place] !=".":
                if row[place] in nums_col:
                    return False
                else:
                    nums_col.append(row[place])

    for square in range(9):
        nums_sq = []
        for row in range(square // 3 * 3, square // 3 * 3 + 3): 
            for col in range(square % 3 * 3, square % 3 * 3 + 3): 
                if board[row][col] !=".":
                    if board[row][col] in nums_sq:
                        return False
                    else:
                        nums_sq.append(board[row][col])

    return True

board = [["5","3",".",  ".","7",".",  ".",".","."]
        ,["6",".",".",  "1","9","5",  ".",".","."]
        ,[".","9","8",  ".",".",".",  ".","6","."]
    
        ,["8",".",".",  ".","6",".",  ".",".","3"]
        ,["4",".",".",  "8",".","3",  ".",".","1"]
        ,["7",".",".",  ".","2",".",  ".",".","6"]
            
        ,[".","6",".",  ".",".",".",  "2","8","."]
        ,[".",".",".",  "4","1","9",  ".",".","5"]
        ,[".",".",".",  ".","8",".",  ".","7","9"]]

print(isvalidsudoku(board))