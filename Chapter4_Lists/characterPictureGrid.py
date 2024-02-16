grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# xSize = int(len(grid[0]))
# ySize = int(len(grid))

# for x in range(xSize):
#     for y in range(ySize):
#         print(grid[y][x],end='')
#     print()

for x in range(len(grid)):
    for y in range(len(grid[x])):
        print(grid[x][y],end='')
    print()

for x in range(len(grid)):
    for y in range(len(grid[x])):
        # Use end='' for all characters except the last one in each row
        if y == len(grid[x]) - 1:
            print(grid[x][y])
        else:
            print(grid[x][y], end='')