# rat in a maze problem
# rat has to move from source (0,0) to destination (m-1,n-1) in a mxn matrix
# rat can only move forward or down

def ratInMaze(maze, sol, i, j, m, n):
    if i==m and j==n:
        sol[m][n] = 1
        for i in range(m+1):
            for j in range(n+1):
                print(sol[i][j],end=' ')
            print()
        print()

        return True

    if i>m or j>n:
        return False

    if maze[i][j]=='x':
        return False

    # assume sol exists through current cell
    sol[i][j] = 1

    rightSuccess = ratInMaze(maze, sol, i, j+1, m, n)
    downSuccess = ratInMaze(maze, sol, i+1, j, m,n)

    # backtracking
    sol[i][j] = 0

    if rightSuccess or downSuccess:
        return True

    return False


if __name__=='__main__':
    maze = [['0','0','x','0'],
            ['0','0','0','0'],
            ['0','x','0','0'],
            ['x','0','0','0']]
    m = 4
    n = 4
    sol = [[0 for _ in range(n)] for _ in range(m)]
    ans = ratInMaze(maze, sol, 0, 0, m-1, n-1)
    if ans == False:
        print('Path does not exist')
