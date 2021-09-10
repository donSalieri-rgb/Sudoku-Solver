def solve(bo):
    """
    
    Sovles the board using backtracking
    :param bo : 2d list on integers
    :return: solution

    """
    find = find_empty(bo)
    if not find:
        return True
    else: 
        row, col = find
    
    for i in range(1,10):
        if valid(bo, i , (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0 # Empties the block if not valid with number i.
    return False

# Check if entered number is valid

def valid(bo, num ,pos):
    
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    #Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    #Check row
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    #Check box

    #Finds the position of the block in the grid.
    box_x=pos[1] // 3 # Position of the block from top.
    box_y=pos[0] // 3 # Position of the block from left.

    for i in range(box_y*3, box_y*3 +3): # Traversing the particular block
        for j in range(box_x*3, box_x*3 +3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True

    # Print the Board.

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0: # create a division of every block
            print("- - - - - - - - - - - - - ") 
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:   # create a division of every block
                print(" | ", end="")
            
            if j==8:
                print(bo[i][j]) # send control to new line after row end
            else:
                print(str(bo[i][j]) + " ",end="")

#  Find an empty box.

def find_empty(bo): 

    """
    finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0: # Considering 0 as an empty block.
                return (i,j) # row, col ( will be returned as a Tuple )
    return None