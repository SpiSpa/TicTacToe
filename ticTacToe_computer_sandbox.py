import numpy as np
import random as rand

myArray = np.zeros([3, 3])
print(myArray)

cornerList = [[0, 0], [0, 2], [2, 0], [2, 2]]
nonCornerList = [[0, 1], [1, 0], [1, 2], [2, 1]]

probNumber = rand.randint(1, 11)
print(probNumber)

#if the computer can win. usually do that
#else if the player is gonna win, usually do that.
for i in range(9):
    if myArray[1, 1] == 0:
        if probNumber in range(1, 3):
            newRand = rand.randint(0, len(cornerList)-1)
            print(newRand)
            myArray[cornerList[newRand][0], cornerList[newRand][1]] = 1
            print(myArray)
            cornerList.pop(newRand)
            print(cornerList)
        elif probNumber == 3:
            newRand = rand.randint(0, len(nonCornerList)-1)
            print(newRand)
            myArray[nonCornerList[newRand][0], nonCornerList[newRand][1]] = 1
            print(myArray)
            nonCornerList.pop(newRand)
            print(nonCornerList)
        else:
            myArray[1, 1] = 1
            print(myArray)
    else:
        if probNumber in range(1, 7):  #throws error when the length of corner list is 0
            newRand = rand.randint(0, len(cornerList)-1)
            print(newRand)
            myArray[cornerList[newRand][0], cornerList[newRand][1]] = 1
            print(myArray)
            cornerList.pop(newRand)
            print(cornerList)
        else:
            newRand = rand.randint(0, len(nonCornerList)-1)
            print(newRand)
            myArray[nonCornerList[newRand][0], nonCornerList[newRand][1]] = 1
            print(myArray)
            nonCornerList.pop(newRand)
            print(nonCornerList)
        #else if the middle is taken
        


