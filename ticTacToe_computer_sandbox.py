import numpy as np
import random as rand

myArray = np.zeros([3, 3])
print(myArray)
cornerList = [[0, 0], [0, 2], [2, 0], [2, 2]]
nonCornerList = [[0, 1], [1, 0], [1, 2], [2, 1]]

for i in range(5):
    

    probNumber = rand.randint(1, 10)
    print("first Probabiity number", probNumber)

    #if the computer can win. usually do that
    def checkWins():
        columnCheck = myArray.sum(axis=0)
        rowCheck = myArray.sum(axis=1)
        diagonalDownCheck = myArray[0, 0] + myArray[1, 1] + myArray[2, 2]
        diagonalUpCheck = myArray[2, 0] + myArray[1, 1] + myArray[0, 2]

        #check if the computer can win.
        for i in range(3):   #check the columns, then the rows
            if ((columnCheck[i] == 2) and (probNumber in range(1, 9))):
                myArray[0, i] = 1
                myArray[1, i] = 1
                myArray[2, i] = 1
                print("Computer wins!")
                print(myArray)
                return(True)
            elif ((rowCheck[i] == 2) and (probNumber in range(1, 9))):
                myArray[i, 0] = 1
                myArray[i, 1] = 1
                myArray[i, 2] = 1
                print("Computer wins!")
                print(myArray)
                return(True)
        if ((diagonalDownCheck == 2) and (probNumber in range(1, 9))):
            myArray[0, 0] = 1
            myArray[1, 1] = 1
            myArray[2, 2] = 1
            print("Computer wins!")
            return(True)
        elif ((diagonalUpCheck == 2) and (probNumber in range(1, 9))):
            myArray[0, 2] = 1
            myArray[1, 1] = 1
            myArray[2, 0] = 1
            print("Computer wins!")
            return(True)

        #check if the opponent can win.
        for i in range(3):   #check the columns, then the rows
            if ((columnCheck[i] == -2) and (probNumber in range(1, 9))):
                if myArray[0, i] == 0:
                    myArray[0, i] = 1
                elif myArray[1, i] == 0:
                    myArray[1, i] = 1
                elif myArray[2, i] == 0:
                    myArray[2, i] = 1
                print(myArray)
                return(True)
            elif ((rowCheck[i] == -2) and (probNumber in range(1, 9))):
                if myArray[i, 0] == 0:
                    myArray[i, 0] = 1
                elif myArray[i, 1] == 0:
                    myArray[i, 1] = 1
                elif myArray[i, 2] == 0:
                    myArray[i, 2] = 1
                print(myArray)
                return(True)
        if ((diagonalDownCheck == -2) and (probNumber in range(1, 9))):
            if myArray[0, 0] == 0:
                myArray[0, 0] = 1
            elif myArray[1, 1] == 0:
                myArray[1, 1] = 1
            elif myArray[2, 2] == 0:
                myArray[2, 2] == 1
            return(True)
        
        elif ((diagonalUpCheck == -2) and (probNumber in range(1, 9))):
            if myArray[0, 2] == 0:
                myArray[0, 0] = 1
            elif myArray[1, 1] == 0:
                myArray[1, 1] = 1
            elif myArray[2, 0] == 0:
                myArray[2, 2] == 1
            return(True)
        return(False)
    
    def normalMove():
        # This is what the computer does if it's not blocking an opponent win
        if myArray[1, 1] == 0:
            if (((len(cornerList) == 0) and (len(nonCornerList) == 0)) or (probNumber in range(4, 11))):
                myArray[1, 1] = 1   #usually choses the middle space
                print(myArray)
            elif (((probNumber in range(1, 3)) and (len(cornerList) > 0)) or (len(nonCornerList) == 0)): #occasionaly chooses a corner space
                newRand = rand.randint(0, len(cornerList)-1)
                print(newRand)
                myArray[cornerList[newRand][0], cornerList[newRand][1]] = 1
                print(myArray)
                cornerList.pop(newRand)
                print(cornerList)
            elif probNumber == 3:  #rarely chooses a noncorner, nonmiddle space
                newRand = rand.randint(0, len(nonCornerList)-1)
                print(newRand)
                myArray[nonCornerList[newRand][0], nonCornerList[newRand][1]] = 1
                print(myArray)
                nonCornerList.pop(newRand)
                print(nonCornerList)
            
        else:
            if (((probNumber in range(1, 7)) and (len(cornerList) > 0)) or (len(nonCornerList) == 0)):
                newRand = rand.randint(0, len(cornerList)-1)
                print("second new rand", newRand)
                myArray[cornerList[newRand][0], cornerList[newRand][1]] = 1
                print(myArray)
                cornerList.pop(newRand)
                print("corner list: ", cornerList)
            elif ((len(cornerList) == 0) and (len(nonCornerList) == 0)):
                myArray[1, 1] = 1
                print(myArray)
            else:
                newRand = rand.randint(0, len(nonCornerList)-1)
                print(newRand)
                print(nonCornerList[newRand])
                myArray[nonCornerList[newRand][0], nonCornerList[newRand][1]] = 1
                print(myArray)
                nonCornerList.pop(newRand)
                print(nonCornerList)

    if checkWins() == False:
        normalMove()
        
        
        


