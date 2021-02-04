import random

def bubbleSort(inputList):

    for i in range(len(inputList)):
        counter = 0
        for i in range(len(inputList)-1):
            a = inputList[i]
            b = inputList[i+1]

            if a > b:
                inputList[i] = b
                inputList[i+1] = a
            else:
                counter += 1
            
        
        if counter == len(inputList)-1:
            print(counter)
            break
        
    return(inputList)


if __name__ == "__main__":
    n = 20
    testList = random.sample(list(range(100)),20)

    print('Unsorted List:')
    print(testList)

    print('Sorted List')
    print(bubbleSort(testList))

