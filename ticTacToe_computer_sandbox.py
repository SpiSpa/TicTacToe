import numpy as np
import random as rand

myArray = np.zeros([3, 3])

cornerList = [[0, 0], [0, 2], [2, 0], [2, 2]]
nonCornerList = [[0, 1], [1, 0], [1, 2], [2, 1]]

    
def computerPlayer():
    probNumber = rand.randint(1, 10)
    computerPlayerTurn = ""
    
    #if the computer can win. usually do that
    def checkWins():
        global computerPlayerTurn
        columnCheck = myArray.sum(axis=0)
        rowCheck = myArray.sum(axis=1)
        diagonalDownCheck = myArray[0, 0] + myArray[1, 1] + myArray[2, 2]
        diagonalUpCheck = myArray[2, 0] + myArray[1, 1] + myArray[0, 2]

        #check if the computer can win.
        for i in range(3):   #check the columns, then the rows
            if ((columnCheck[i] == 2) and (probNumber in range(1, 9))):
                for j in range(3):
                    if myArray[j, i] == 0:
                        myArray[j, i] = 1
                        computerPlayerTurn = str(j) + str(i)
                        return(computerPlayerTurn)
            elif ((rowCheck[i] == 2) and (probNumber in range(1, 9))):
                for j in range (3):
                    if myArray[i, j] == 0:
                        myArray[i, j] = 1
                        computerPlayerTurn = str(i) + str(j)
                        return(computerPlayerTurn)
        if ((diagonalDownCheck == 2) and (probNumber in range(1, 9))):
            for i in range(3):
                if myArray[i, i] == 0:
                    myArray[i, i] = 1
                    computerPlayerTurn = str(i) + str(i)
                    return(computerPlayerTurn)
        elif ((diagonalUpCheck == 2) and (probNumber in range(1, 9))):
            for i in range(3):
                if myArray[0+i, 2-i] == 0:
                    myArray[0+i, 2-i] = 1
                    computerPlayerTurn = str(0+i) + str(2-i)
                    return(computerPlayerTurn)
            

        #check if the opponent can win.
        for i in range(3):   #check the columns, then the rows
            if ((columnCheck[i] == -2) and (probNumber in range(1, 9))):
                for j in range(3):
                    if myArray[j, i] == 0:
                        myArray[j, i] = 1
                        computerPlayerTurn = str(j) + str(i)
                        return(computerPlayerTurn)
                    
            elif ((rowCheck[i] == -2) and (probNumber in range(1, 9))):
                for j in range(3):
                    if myArray[i, j] == 0:
                        myArray[i, j] = 1
                        computerPlayerTurn = str(i) + str(j)
                        return(computerPlayerTurn)
                
        if ((diagonalDownCheck == -2) and (probNumber in range(1, 9))):
            for i in range(3):
                if myArray[i, i] == 0:
                    myArray[0, 0] = 1
                    computerPlayerTurn = str(i) + str(i)
                    return(computerPlayerTurn)
        
        elif ((diagonalUpCheck == -2) and (probNumber in range(1, 9))):
            for i in range(3):
                if myArray[0+i, 2-i] == 0:
                    myArray[0+i, 2-i] = 1
                    computerPlayerTurn = str(0+i) + str(2-i)
                    return(computerPlayerTurn)
        return("")

    def normalMove():
        # This is what the computer does if it's not blocking an opponent win
        if myArray[1, 1] == 0:
            if (((len(cornerList) == 0) and (len(nonCornerList) == 0)) or (probNumber in range(4, 11))):
                myArray[1, 1] = 1   #usually choses the middle space
                computerPlayerTurn = '11'
                return(computerPlayerTurn)
            
            elif (((probNumber in range(1, 3)) and (len(cornerList) > 0)) or (len(nonCornerList) == 0)): #occasionaly chooses a corner space
                newRand = rand.randint(0, len(cornerList)-1)
                myArray[cornerList[newRand][0], cornerList[newRand][1]] = 1
                computerPlayerTurn = str(cornerList[newRand][0]) + str(cornerList[newRand][1])
                cornerList.pop(newRand)
                return(computerPlayerTurn)
            
            elif probNumber == 3:  #rarely chooses a noncorner, nonmiddle space
                newRand = rand.randint(0, len(nonCornerList)-1)
                myArray[nonCornerList[newRand][0], nonCornerList[newRand][1]] = 1
                computerPlayerTurn = str(nonCornerList[newRand][0]) + str(nonCornerList[newRand][1])
                nonCornerList.pop(newRand)
                return(computerPlayerTurn)
                
        else:
            if (((probNumber in range(1, 7)) and (len(cornerList) > 0)) or (len(nonCornerList) == 0)):
                newRand = rand.randint(0, len(cornerList)-1)
                myArray[cornerList[newRand][0], cornerList[newRand][1]] = 1
                computerPlayerTurn = str(cornerList[newRand][0]) + str(cornerList[newRand][1])
                cornerList.pop(newRand)
                return(computerPlayerTurn)

            elif ((len(cornerList) == 0) and (len(nonCornerList) == 0)):
                myArray[1, 1] = 1
                computerPlayerTurn = "11"
                return(computerPlayerTurn)
                
            else:
                newRand = rand.randint(0, len(nonCornerList)-1)
                myArray[nonCornerList[newRand][0], nonCornerList[newRand][1]] = 1
                computerPlayerTurn = str(nonCornerList[newRand][0]) + str(nonCornerList[newRand][1])
                nonCornerList.pop(newRand)
                return(computerPlayerTurn)

    computerPlayerTurn = checkWins()
    
    if computerPlayerTurn == "":
        computerPlayerTurn = normalMove()
        
    print("turn from smaller functions:" + computerPlayerTurn)
    print(myArray)

    return(computerPlayerTurn)

            
            


