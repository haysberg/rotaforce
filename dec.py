#This file contains the functions used to process the decimal alphabet for rotaforce

def incrementinputString(inputString, value):
    """This function is used to display a given array, when we add a certain value to each member of the array
    
    Arguments:
        inputString {string} -- The integer array that we will brute force
        value {integer} -- The offset that we want our final result to have. It is added to the original number.
    """
    res = []

    #For each numbers in the array given, we add the value provided in the second parameter. We use a modulo because we don't want any number to reach 10.
    #It should go back to 0 instead.
    for a in inputString :
        if str.isdigit(a) :
            res.append((int(a) + value) % 10)
        else:
            res.append(a)
    #We print the result, and add a second argument to print() in order to avoid the numbers to be printed one by line. We want a line to equal a result.
    return res


def incrementalNumber(numberString, offset):
    """This is the function called in our brute.py file, so it is used to call all the other functions.
       This is why it is declared last, because it uses the functions declared previously.
    
    Arguments:
        numberString {string} -- The input string containing only numbers that we get from the user.
        offset {integer} -- The offset that we want to have for our possible unciphered text
    """
    return incrementinputString(numberString, offset)

        