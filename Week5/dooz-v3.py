def rowColWinner(doozCell):
    if doozCell == 'x':
        winner = 1
    elif doozCell == 'o':
        winner = 2
    else:
        winner=0
    return winner

def checkWinner(doozTable):
    """
    checks the winner of the dooz game
    INPUT: 
    doozTable which is a list of lists 3*3 
    OUTPUT:
    winner: 0:no winner, 1: user1 , 2: user2
    """
    winner = 0
    for row in doozTable: #check the rows
        if row[0] == row[1] and row[1] == row[2]:
            winner = rowColWinner(row[0])
            # if row[0] == 'x':
            #     winner = 1
            # else:
            #     winner = 2
            break 
    for col in range(3): #check columns
        if doozTable[0][col] == doozTable[1][col] and doozTable[1][col] == doozTable[2][col]:
            # if doozTable[0][col] == 'x':
            #     winner = 1
            # else:
            #     winner = 2
            winner = rowColWinner(doozTable[0][col])
            break
    if doozTable[0][0] == doozTable[1][1] == doozTable[2][2]:
        winner = rowColWinner(doozCell=doozTable[0][0]) 
    if doozTable[0][2] == doozTable[1][1] == doozTable[2][0]:
        winner = rowColWinner(doozTable[0][2])
    return winner 

doozTable = [['x',' ',' '],[' ', 'x','o'],[' ', ' ', ' ']]
winner = checkWinner(doozTable)
print(winner)