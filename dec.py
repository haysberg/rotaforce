import sys

def stringToIntegerArray(inputString):
    res = []
    for i in range(len(inputString)) :
        res.append(ord(inputString[i]) - 48)
    return res

def incrementIntArray(intArray, value):
    res = []
    for a in intArray :
        res.append((a + value) % 10)
    print(res, end='')

def incrementalNumber(numberString):
    integerArray = stringToIntegerArray(numberString)
    for i in range(9):
        incrementIntArray(integerArray, i)
        print('')

        