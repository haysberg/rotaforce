def incrementCharArray(charArray, value):
    """This function is used to display a given array, when we add a certain value to each member of the array
    
    Arguments:
        charArray {string} -- The string that we have in input and that we want to bruteforce
        value {integer} -- How much offset we want from the input string. If you have value = 3, A will become D.
    """
    res = []

    #For each character in the array given, we add the value provided in the second parameter.
    #We use a modulo because we don't want any character ASCII code be greater than 122.
    #It should go back to 97 instead, which is the ASCII code for the letter A.
    for a in charArray :
        if str.isalpha(a) :
            res.append(chr((ord(a)+value - 97) % 26 + 97))
        else:
            res.append(a)

    #We return the string that is obtained from the function to print it later.
    return res



def incrementalChar(charString, offset):
    """This is the function called in our brute.py file, so it is used to call all the other functions.
       This is why it is declared last, because it uses the function declared previously.
    
    Arguments:
        charString {string} -- The string that we want to brute force.
        offset {integer} -- The offset that we want to give to our potential unciphered text
    """
    return incrementCharArray(charString, offset)

        