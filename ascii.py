def incrementString(String, value):
    """This function is used to display a given string, when we add a certain value to each member of the string.
    ABC with an offset of 3 will become DEF.
    
    Arguments:
        String {string} -- The string that we will increment
        value {integer} -- The offset that we want to give to the string
    """
    res = []

    #For each character in the array given, we add the value provided in the second parameter.
    #We use a modulo because we don't want any character ASCII code be greater than 128.
    #It should go back to 97 instead, which is the ASCII code for the letter A.
    for a in String :
        res.append(chr( (ord(a)+value) % 128))


    #We print the result, and add a second argument to print() in order to avoid the characters to be printed one by line. We want a line to equal a result.
    for c in res :
        print(c, end='')


    #For this specific feature, I needed to print something to show the limits between the different results as there is some special characters that mess up with the lines.
    #We add a return character at the start of the line to avoid it being after a word.
    print('\n-----------------')


def incrementalASCII(inputString):
    """This is the function called in our brute.py file, so it is used to call all the other functions.
    This is why it is declared last, because it uses the function declared previously.

    Arguments:
        inputString {string} -- The string that we will brute force and increment.
    """

    #We add numbers to the array, from 0 to 127. The incrementString will give us the results in the terminal.
    for i in range(127):
        incrementString(inputString, i)
        #When we have a new possible plaintext calculated, we return to the line for more visibility
        print('')

        