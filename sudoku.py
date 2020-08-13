def parseGrid(string):
    if len(string) != 81:
        return False

    grid = []
    for i in range(9):
        grid.append(list(string[i * 9 : (i + 1) * 9]))
    return grid 

def validInsertion(board, y, x, num):
    for i in range(9):
        boxRow = (y // 3) * 3 + (i // 3)
        boxCol = (x // 3) * 3 + (i % 3)
        if board[y][i] != '.' and int(board[y][i]) == num:
            return False
        if board[i][x] != '.' and int(board[i][x]) == num:
            return False
        if board[boxRow][boxCol] != '.' and int(board[boxRow][boxCol]) == num:
            return False
    return True

def backtrack(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != '.':
                continue
            for i in range(1, 10):
                if not validInsertion(grid, row, col, i):
                    continue
                grid[row][col] = str(i)
                b = backtrack(grid)
                if b:
                    return b
                else:
                    grid[row][col] = '.'
            return False
    return grid

def sudokuSolver(string):
    grid = parseGrid(string)
    success = backtrack(grid)
    
    return success if success else "No valid solution found"
    

print(sudokuSolver('..3.2.6..9..3.5..1..18.64....81.29..7..........67.82....26.95..8..2.3..9..5.1.3..'))
