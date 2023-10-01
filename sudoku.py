grid = [ [0,7,0,0,6,8,3,0,9],
          [0,0,0,0,0,2,0,0,5],
          [0,6,4,7,0,0,8,0,0],
          [0,9,6,0,0,4,0,0,3],
          [8,3,0,0,0,0,0,9,1],
          [4,0,0,3,0,0,2,7,0],
          [0,0,3,0,0,7,6,2,0],
          [9,0,0,8,0,0,0,0,0],
          [6,0,8,2,5,0,0,3,0] ]

def solve(grid):
    empty = empty_cell(grid)
    if not empty:
        return True
    else:
        row, column = empty
    
    for i in range(1, 10):
        if check(grid, i, (row, column)):
            grid[row][column] = i

            if solve(grid):
                return True
    
    grid[row][column] = 0
        
    return False


def check(grid, number, position):
    #check in the row
    for i in range(len(grid[0])):
        if grid[position[0]][i] == number and position[1] != i:
            return False

    #check in the column
    for i in range(len(grid)):
        if grid[i][position[1]] == number and position[0] != i:
            return False

    #check inside the block
    block_x = position[1] // 3
    block_y = position[0] // 3
    
    for i in range(block_y * 3, block_y * 3 + 3):
        for j in range(block_x * 3, block_x * 3 + 3):
            if grid[i][j] == number and (i, j) != position:
                return False
    
    return True


def output(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("---------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " " , end="" )


def empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if(grid[i][j] == 0):
                return (i, j)
    
    return None 

output(grid)
print("______________________")
solve(grid)
output(grid)