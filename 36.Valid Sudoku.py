class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j]!=".":
                        k=board[i][j]
                        board[i][j]='.'
                        if isvalid(board,i,j,board[i][j],k)==False:
                            return False
                        board[i][j]=k
            return True
        def isvalid(board,row,col,c,k):
            for i in range(9):
                if  board[row][i]==k:
                    return False
                if board[i][col]==k:
                    return False
                if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)]==k:
                    return False
            return True
        return solve(board)
