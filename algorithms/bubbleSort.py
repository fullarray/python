def bubbleSorting(myNumList):
    moreSwaps = True
    while moreSwaps:
        moreSwaps = False
        for element in range(len(myNumList)-1):
            if myNumList[element] > myNumList[element+1]:
                moreSwaps = True
                temp = myNumList[element]
                myNumList[element] = myNumList[element+1]
                myNumList[element+1]=temp
    return myNumList

#This is the main driver program
def bubbleSortingTest():
    myNumList = [4,5,3,9,29,3,4,65]
    sortedList = bubbleSorting(myNumList)
    print(sortedList)
