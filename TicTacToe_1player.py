''' Chapter 7, question 11 - tic tac toe with a computer player and a human player'''

import numpy as np
import random as rand

gameBoard = np.zeros([3, 3])
gameCount = 0
cornerList = [[0, 0], [0, 2], [2, 0], [2, 2]]  #these help the computer's strategy
nonCornerList = [[0, 1], [1, 0], [1, 2], [2, 1]]  #this list helps computer keep track of move options

print('\nWelcome to Tic-Tac-Toe!')
print('On your turn, choose where to put your marker')
print('by inputing the index. \n')
print('Three in a row - any direction - and you WIN! \n')

initialDisplay = np.full((3, 3), "___")
print(initialDisplay)

def getPlayerMove(XorO):  # get and validate player's turn
    global cornerList
    global nonCornerList

    checkValues = False
    timeToPopCorner = False
    timeToPopSide = False

    while (checkValues == False):
        player = input("where do you want your " + XorO + " ? enter as pair of numbers\n")
        player = player.replace(" ", "")
        
        #check that it's exactly two integers
        if (not player.isdecimal() or (len(player) != 2)): 
            print("ERROR: enter two digits. 0, 1, or 2\n")
        else:
            a = int(player[0])
            b = int(player[1])

            #check that the integers are both 0, 1, or 2
            if ((a < 0 or a > 3) or (b < 0 or b > 3)):
                print("ERROR:  input out of range. Enter two digits. 0, 1, or 2\n")
        
            else:   
                if((gameBoard[a, b]) != 0):
                    print("Error!  Space has already been played!")
                    print("Enter a location with no X or O.\n")
                else:
                    checkValues = True

    #manage corner and side element lists for computer player. remove items computer can't use
    for i in range(len(cornerList)):
        
        if ((cornerList[i][0] == a) and (cornerList[i][1] == b)):
            popIndex = i
            timeToPopCorner = True
    if (timeToPopCorner == True):
        cornerList.pop(popIndex)
    for i in range(len(nonCornerList)):
        if ((nonCornerList[i][0] == a) and (nonCornerList[i][1] == b)):
            popIndex = i
            timeToPopSide = True
    if (timeToPopSide == True):
        nonCornerList.pop(popIndex)

    #turn player's choice into string for returning both values
    playerChoice = str(a) + str(b)
    print("player choice: " + playerChoice)
    return(playerChoice)

def boardManager(player, XorO):    #updates game board
    global gameBoard
    a = int(player[0])
    b = int(player[1])
    
    gameBoard[a, b] = XorO

def gameDisplay(negValue, posValue): #displays game board as x's and o's
    global gameBoard
    displayBoard = np.full((3, 3), "   ")

    for i in range(3):
        for j in range(3):
            if gameBoard[i, j] == 0:
                displayBoard[i, j] = "___"
            elif gameBoard[i, j] == -1:
               displayBoard[i, j] = negValue
            else:
               displayBoard[i, j] = posValue
            
    print(displayBoard)

def winCheck(): #determines if there is a winner or a draw
    global gameCount

    gameCount += 1

    for i in range(3):
        #check each row for three 1's or three -1's
        if ((np.sum(gameBoard[i]) == 3) or (np.sum(gameBoard[i]) == -3)): 
            print("we have a winner!")
            return(True)
        
        #check each column for three 1's or three -1's
        elif ((np.sum(gameBoard[:,i]) == 3) or (np.sum(gameBoard[:,i]) == -3)):
            print("we have a winner!")
            return(True)
        
    #find the sum of each diagonal
    diagonalDownCheck = gameBoard[0, 0] + gameBoard[1, 1] + gameBoard[2, 2]
    diagonalUpCheck = gameBoard[2, 0] + gameBoard[1, 1] + gameBoard[0, 2]

    #check each diagonal for three 1's or there -1's
    if ((diagonalDownCheck == 3) or (diagonalDownCheck == -3)): 
        print("we have a winner!")
        return(True)
    elif ((diagonalUpCheck == 3) or (diagonalUpCheck == -3)): 
        print("we have a winner!")
    elif (gameCount == 10):  #account for the first winCheck at the beginning of the loop in gameManager
        print("DRAW!")
        return(True)
    else:
        return(False)
    
def computerPlayer():
    probNumber = rand.randint(1, 10) #randomize the computer's move.  doesn't always do best move.
    computerPlayerTurn = ""
    
    #computer checks if there is a way for it or it's opponent to win
    def checkWins():
        global computerPlayerTurn
        global cornerList
        global nonCornerList
        columnCheck = gameBoard.sum(axis=0)
        rowCheck = gameBoard.sum(axis=1)
        diagonalDownCheck = gameBoard[0, 0] + gameBoard[1, 1] + gameBoard[2, 2]
        diagonalUpCheck = gameBoard[2, 0] + gameBoard[1, 1] + gameBoard[0, 2]

        #check if the computer can win.
        for i in range(3):   #check the columns, then the rows
            if ((columnCheck[i] == 2) and (probNumber in range(1, 9))):
                for j in range(3):
                    if gameBoard[j, i] == 0:
                        computerPlayerTurn = str(j) + str(i)
                        return(computerPlayerTurn)
            elif ((rowCheck[i] == 2) and (probNumber in range(1, 9))):
                for j in range (3):
                    if gameBoard[i, j] == 0:
                        computerPlayerTurn = str(i) + str(j)
                        return(computerPlayerTurn)
        if ((diagonalDownCheck == 2) and (probNumber in range(1, 9))):
            for i in range(3):
                if gameBoard[i, i] == 0:
                    computerPlayerTurn = str(i) + str(i)
                    return(computerPlayerTurn)
        elif ((diagonalUpCheck == 2) and (probNumber in range(1, 9))):
            for i in range(3):
                if gameBoard[0+i, 2-i] == 0:
                    computerPlayerTurn = str(0+i) + str(2-i)
                    return(computerPlayerTurn)
            

        #check if the opponent can win.
        for i in range(3):   #check the columns, then the rows
            if ((columnCheck[i] == -2) and (probNumber in range(1, 9))):
                for j in range(3):
                    if gameBoard[j, i] == 0:
                        computerPlayerTurn = str(j) + str(i)
                        return(computerPlayerTurn)
                    
            elif ((rowCheck[i] == -2) and (probNumber in range(1, 9))):
                for j in range(3):
                    if gameBoard[i, j] == 0:
                        computerPlayerTurn = str(i) + str(j)
                        return(computerPlayerTurn)
                
        if ((diagonalDownCheck == -2) and (probNumber in range(1, 9))):
            for i in range(3):
                if gameBoard[i, i] == 0:
                    computerPlayerTurn = str(i) + str(i)
                    return(computerPlayerTurn)
        
        elif ((diagonalUpCheck == -2) and (probNumber in range(1, 9))):
            for i in range(3):
                if gameBoard[0+i, 2-i] == 0:
                    computerPlayerTurn = str(0+i) + str(2-i)
                    return(computerPlayerTurn)
        return("")

    def normalMove():
        # This is what the computer does if it's not blocking an opponent or winning
        if gameBoard[1, 1] == 0: #this is what it does if the middle is still open
            #usually chooses the middle space
            if (((len(cornerList) == 0) and (len(nonCornerList) == 0)) or (probNumber in range(4, 11))):
                computerPlayerTurn = '11'
                return(computerPlayerTurn)
            
            #occasionally chooses a corner
            elif (((probNumber in range(1, 3)) and (len(cornerList) > 0)) or (len(nonCornerList) == 0)): 
                newRand = rand.randint(0, len(cornerList)-1)
                computerPlayerTurn = str(cornerList[newRand][0]) + str(cornerList[newRand][1])
                cornerList.pop(newRand)
                return(computerPlayerTurn)
            
            elif probNumber == 3:  #rarely chooses a noncorner, nonmiddle space
                newRand = rand.randint(0, len(nonCornerList)-1)
                computerPlayerTurn = str(nonCornerList[newRand][0]) + str(nonCornerList[newRand][1])
                nonCornerList.pop(newRand)
                return(computerPlayerTurn)
                
        else:  #what to do if middle space is already taken
            #  usually chose a corner, unless all sides are taken.  then computer has to choose a corner
            if (((probNumber in range(1, 7)) and (len(cornerList) > 0)) or (len(nonCornerList) == 0)):
                newRand = rand.randint(0, len(cornerList)-1)
                computerPlayerTurn = str(cornerList[newRand][0]) + str(cornerList[newRand][1])
                cornerList.pop(newRand)
                return(computerPlayerTurn)
            
            # on the off chance the middle is still available and all other spots are taken
            elif ((len(cornerList) == 0) and (len(nonCornerList) == 0)):
                computerPlayerTurn = "11"
                return(computerPlayerTurn)
            
            # sometimes chose a side, unless all the corners are taken, then computer has to choose a side.
            else:
                newRand = rand.randint(0, len(nonCornerList)-1)
                computerPlayerTurn = str(nonCornerList[newRand][0]) + str(nonCornerList[newRand][1])
                nonCornerList.pop(newRand)
                return(computerPlayerTurn)

    #checks if there is a way to win or block first
    computerPlayerTurn = checkWins()
    
    #if there's not a way to win or block, proceede to normal move
    if computerPlayerTurn == "":
        computerPlayerTurn = normalMove()
        
    print("Computer's move:" + computerPlayerTurn)
    return(computerPlayerTurn)

def gameManager2():  # if player wants to be "O" go here.
    while (winCheck() == False):   
        player1 = computerPlayer() #computer chooses move
        boardManager(player1, 1)  # update game board
        gameDisplay(" O ", " X ")

        if (winCheck()) == True:  
            break
        player2 = getPlayerMove('O') #player chooses move
        boardManager(player2, -1) #update game board
        gameDisplay(" O ", " X ")

def gameManager1(): #if player wants to be "X" go here.
    while (winCheck() == False):
        player1 = getPlayerMove('X') #player chooses move
        boardManager(player1, -1) #update game board
        gameDisplay(" X ", " O ")

        if (winCheck()) == True:
            break
        
        player2 = computerPlayer() #computer chooses Move
        boardManager(player2, 1) #updage game board
        gameDisplay(" X ", " O ")

#here's the "main" program.
        

whoGoesFirst = input("Would you like to play X or O? \n")

if ((whoGoesFirst =='x') or (whoGoesFirst =='X')):
    gameManager1()
else:
    gameManager2()



