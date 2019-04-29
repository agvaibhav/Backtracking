
def solveNQueen(board ,i, n):
    # base case
    if i==n:
        # you have successfully placed queens in n rows (0....n-1)
        # print the board
        for i in range(n):
            for j in range(n):
                if board[i][j]==1:
                    print('Q',end=' ')
                else:
                    print(board[i][j],end=' ')
            print()
        print()
                
        #return True  # to print only the first board
        return False   # to print all the possible boards

    # rec case
    # try to place the queen in current row and call rec on the remaining part
    for j in range(n):
        if isSafe(board, i,j,n):
            board[i][j]=1

            if solveNQueen(board, i+1, n):
                return True

            board[i][j]='-'   # backtracking

    return False


def isSafe(board, i, j, n):
    # to check for col
    for row in range(i):
        if board[row][j]==1:
            return False

    # to check for upper left diagonal
    for r,c in zip(range(i,-1,-1), range(j,-1,-1)):
        if board[r][c]==1:
            return False

    # to check for upper right diagonal
    for r,c in zip(range(i,-1,-1), range(j,n,1)):
        if board[r][c]==1:
            return False

    return True

if __name__=='__main__':
    n = int(input('write the size of the board'))
    board = [['-' for _ in range(n)] for _ in range(n)]
    solveNQueen(board, 0, n)
