import numpy as np

gameBoard = np.full([3, 3], '___')
gameCount = 0


print('\nWelcome to Tic-Tac-Toe!')
print('On your turn, choose where to put your marker')
print('by inputing the index. \n')
print('Three in a row - any direction - and you WIN! \n')

print(gameBoard)

def getPlayerMove(XorO):

    checkValues = False

    while (checkValues == False):
    #get and validate player 1's turn.  send result to check if the 
        player = input("where do you want your " + XorO + " ? enter as pair of numbers\n")
        player = player.replace(" ", "")
        
        if (not player.isdecimal() or (len(player) != 2)):
            print("ERROR: enter two digits. 0, 1, or 2\n")
        else:
            a = int(player[0])
            b = int(player[1])

            if ((a < 0 or a > 3) or (b < 0 or b > 3)):
                print("ERROR:  input out of range. Enter two digits. 0, 1, or 2\n")
        
            else:   
                if((gameBoard[a, b]) != '___'):
                    print("Error!  Space has already been played!")
                    print("Enter a location with no X or O.\n")
                else:
                    checkValues = True

    playerChoice = str(a) + str(b)
       
    return(playerChoice)

def boardManager(player, XorO):    #update game board
    global gameBoard
    a = int(player[0])
    b = int(player[1])
    
    gameBoard[a, b] = XorO
    print(gameBoard)
    
def winCheck():
    global gameCount

    gameCount += 1

    for i in range(3):
        if (all(el == ' X ' for el in gameBoard[i])) or (all(el == ' O ' for el in gameBoard[i])): 
            print("we have a winner!")
            return(True)

        elif (all(el == ' X ' for el in gameBoard[:, i])) or (all(el == ' O ' for el in gameBoard[:, i])): 
            print("we have a winner!")
            return(True)
        
    if (gameBoard[0, 0] == ' X ' and gameBoard[1, 1] == ' X ' and gameBoard[2, 2] == ' X '): 
        print("we have a winner!")
        return(True)
    elif (gameBoard[0, 0] == ' O ' and gameBoard[1, 1] == ' O ' and gameBoard[2, 2] == ' O '): 
        print("we have a winner!")
        return(True)
    elif (gameBoard[0, 2] == ' X ' and gameBoard[1, 1] == ' X ' and gameBoard[2, 0] == ' X '): 
        print("we have a winner!")
        return(True)
    elif (gameBoard[0, 2] == ' O ' and gameBoard[1, 1] == ' O ' and gameBoard[2, 0] == ' O '): 
        print("\nWe have a winner!")
        return(True)
    elif (gameCount == 10):  #account for the first winCheck at the beginning of the loop in gameManager
        print("DRAW!")
        return(True)
    else:
        return(False)

def gameManager():
    while (winCheck() == False):
        
        player1 = getPlayerMove('X')
        boardManager(player1, ' X ')
        if (winCheck()) == True:
            break
        player2 = getPlayerMove('O')
        boardManager(player2, ' O ')

gameManager()