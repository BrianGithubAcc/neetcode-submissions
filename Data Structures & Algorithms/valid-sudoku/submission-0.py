class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def colIndex(col):
            seen = set()
            for i in range(9):
                if board[i][col] != '.':
                    if board[i][col] in seen:
                        return False
                    seen.add(board[i][col])
            return True

        def rowIndex(row):
            seen = set()
            for i in range(9):
                if board[row][i] != '.':
                    if board[row][i] in seen:
                        return False
                    seen.add(board[row][i])
            return True
        
        def squareLook():
            for blockRow in range(0, 9, 3):
                for blockCol in range(0, 9, 3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            cell = board[blockRow + i][blockCol + j]
                            if cell != '.':
                                if cell in seen:
                                    return False
                                seen.add(cell)
            return True
        
        for i in range(9):
            if not colIndex(i) or not rowIndex(i):
                return False
        
        if not squareLook():
            return False
        
        return True
