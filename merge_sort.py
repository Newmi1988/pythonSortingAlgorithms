import random

def mergeSort(listInput):
    if len(listInput) < 2:
        return(listInput)
    else:
        n = int(len(listInput)/2)
        leftList =  mergeSort(listInput[:n])
        rightList = mergeSort(listInput[n:])

        return(mergeList(leftList, rightList))

def mergeList(leftList, rightList):
    if not len(leftList) or not len(rightList):
        return(leftList or rightList)

    result = []

    leftCounter,rightCounter = 0, 0
    while (len(result) < len(leftList) + len(rightList)):
        if leftList[leftCounter] < rightList[rightCounter]:
            result.append(leftList[leftCounter])
            leftCounter += 1
        else:
            result.append(rightList[rightCounter])
            rightCounter += 1

        if leftCounter == len(leftList) or rightCounter == len(rightList):
            result.extend(leftList[leftCounter:] or rightList[rightCounter:])
            break

    return(result)
        

if __name__ == "__main__":
    n = 20
    testList = random.sample(list(range(100)),20)

    print('Unsorted List:')
    print(testList)

    print('Sorted List')
    print(mergeSort(testList))

