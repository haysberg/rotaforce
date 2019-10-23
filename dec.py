#This file contains the functions used to process the decimal alphabet for rotaforce


def stringToIntegerArray(inputString):
    """This function is used to transform a string array (the one we get as an argument) into an integer array
    
    Arguments:
        inputString {string} -- The string that we want to convert to an integer
    
    Returns:
        integer -- The integer that we calculated from the string
    """
    res = []
    #For each character in our input array, we get the character, transform it into an integer and remove 48, which is the offset of the numbers in the ASCII table.
    for i in range(len(inputString)) :
        res.append(ord(inputString[i]) - 48)
    return res


def incrementIntArray(intArray, value):
    """This function is used to display a given array, when we add a certain value to each member of the array
    
    Arguments:
        intArray {array<integer>} -- The integer array that we will brute force
        value {integer} -- The offset that we want our final result to have. It is added to the original number.
    """
    res = []

    #For each numbers in the array given, we add the value provided in the second parameter. We use a modulo because we don't want any number to reach 10.
    #It should go back to 0 instead.
    for a in intArray :
        res.append((a + value) % 10)
    #We print the result, and add a second argument to print() in order to avoid the numbers to be printed one by line. We want a line to equal a result.
    for i in res :
        print(i, end='')


def incrementalNumber(numberString):
    """This is the function called in our brute.py file, so it is used to call all the other functions.
       This is why it is declared last, because it uses the functions declared previously.
    
    Arguments:
        numberString {string} -- The input string containing only numbers that we get from the user.
    """
    #We convert the array given by the user in an integer array
    integerArray = stringToIntegerArray(numberString)

    #We add numbers to the array, from 0 to 9. The incrementIntArray will give us the results in the terminal.
    for i in range(10):
        incrementIntArray(integerArray, i)
        #When we have a new possible plaintext calculated, we return to the line for more visibility
        print('')

        