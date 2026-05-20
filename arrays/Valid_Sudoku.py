class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[j][i]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
            
        for boxRow in range(3):
            for boxCol in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[boxRow*3 + i][boxCol*3 + j]
                        if num == '.':
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
