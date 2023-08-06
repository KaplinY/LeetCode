class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def convert(lst):
            res_dct = {lst[i]: 1 for i in range(0, len(lst))}
            return res_dct
        #checking rows
        for i in range(0,9):
            res_dct = convert(board[i])
            dots = board[i].count(".")
            if len(res_dct) != (9 - dots + 1):
                return(False)
        #checking columns
        column = [0]*9
        for i in range (0,9):
            for j in range (0,9):
                column[j] = board[j][i]
            res_dct = convert(column)
            dots = column.count(".")
            if len(res_dct) != (9 - dots + 1):
                return(False) 
        #checking squares
        for f in range (0,7,3):
            n = 0
            m = 3
            for i in range (0,3):
                square = []
                for i in range (f,f+3):
                    for j in range (n,m):
                        square.append(board[i][j])
                res_dct = convert(square)
                dots = square.count(".")
                if len(res_dct) != (9 - dots + 1):
                    return(False)
                n+=3
                m+=3
        return(True)
