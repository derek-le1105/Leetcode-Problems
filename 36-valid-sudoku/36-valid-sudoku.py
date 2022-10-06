class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardMap = {}
       
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                boardMap.setdefault(board[row][col], []).append([row, col])
        
        for num in boardMap: #for every unique number within the board
            boxes = {}
            for i in range(len(boardMap[num])): #for every point that the unique number resides in the board
                pointI = boardMap[num][i]
                for j in range(i+1, len(boardMap[num])):
                    pointJ = boardMap[num][j]
                    
                    if pointI[0] == pointJ[0] or pointI[1] == pointJ[1]: #same row or same column
                        return False
                checkBox = (pointI[0]//3) * 3 + (pointI[1]//3)
                boxes.setdefault(checkBox, [])
                if 1 in boxes[checkBox]:
                    return False
                boxes[checkBox].append(1)
        return True
                
        
        '''[[".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]]'''
            