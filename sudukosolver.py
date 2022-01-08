""" sudoku solver using back tracking """
sud_board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
]

sud_board_fail = [
        [7,8,7,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
]

sud_board_2 =[[0,0,5,0,2,0,6,0,0],
              [0,9,0,0,0,4,0,1,0],
              [2,0,0,5,0,0,0,0,3],
              [0,0,6,0,3,0,0,0,0],
              [0,0,0,8,0,1,0,0,0],
              [0,0,0,0,9,0,4,0,0],
              [3,0,0,0,0,2,0,0,7],
              [0,1,0,9,0,0,0,5,0],
              [0,0,4,0,6,0,8,0,0] ]


sud_board_3 =[[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [3,8,4,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,2] ]

def valid_board(xboard, num, pos):
    """ check if the board is valid """
    # check row
    for row, _board in enumerate(xboard):
        if xboard[pos[0]][row] == num and pos[1] != row:
            return False

    # check column
    for column, _board in enumerate(xboard):
        if xboard[column][pos[1]] == num and pos[0] != column:
            return False


    # check 3x3 boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if xboard[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(xboard):
    """ print out the board """
    for i, brdlst in enumerate(xboard):
        if i % 3 == 0 and i !=0:
            print("- - - - - - - - - - - -")
        for j, board in enumerate(brdlst,0):
            if j % 3 == 0 and j !=0:
                print(" | ", end="")

            if j == 8:
                print(f"{board}")

            else:
                print(str(board) + " ", end="")


def find_empty(xboard):
    """ find an empty space on the board """
    for i, _board  in enumerate(xboard):
        for j, _board in  enumerate(xboard,0):
            if xboard[i][j] == 0:
                return(i,j)
            #return -1
    return None

def solve(xboard):
    """ solve the puzzle """
    find = find_empty(xboard)
    if not find:
        return True

    row, col = find

    for i in range(1,10):
        if valid_board(xboard,i,(row,col)):
            xboard[row][col] = i

            if solve(xboard):
                return True

            xboard[row][col] = 0

    return False


print_board(sud_board_3)
solve(sud_board_3)
print("* * * * * * * * * * * *")
print_board(sud_board_3)
