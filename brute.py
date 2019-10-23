"""
Please find the GitHub repository of this project at https://github.com/Couaque/rotaforce
Code by Téo Haÿs for the BN311 course
"""

#We import the necessary libraries.
#sys is used to stop the execution of the program in case of wrong arguments.
import sys

#We import the incrementalNumber function, which is the only one that we need in dec.py
from dec import incrementalNumber
from alpha import incrementalChar
from ascii import incrementalASCII


#If there is not exactly 3 arguments, we stop the program. The first argument is the name of the script, the others are the alphabet used and the cipheredtext
if(len(sys.argv) != 3):
    sys.exit("Usage : python3 brute.py <charset> <ciphered_text>")


#If there is 3 arguments, we continue the execution. We display the arguments given, for troubleshooting purposes more than anything else
else:
    print("Alphabet chosen : ", sys.argv[1])
    print("The original ciphered text given is : ", sys.argv[2])


#We set local variables instead of using the sys.argv array, to make it easier to read. It would be more memory efficient to use sys.argv but the overhead is minimal.
alphabet = sys.argv[1]
ciphertext = sys.argv[2]


#This is the equivalent of a switch statement. This will allow us to choose the right function depending of the alphabet choosen.
if(alphabet == "dec"):
    print('The 10 different combinations are : ')
    incrementalNumber(ciphertext)

elif(alphabet == "alpha"):
    print('The 26 different combinations are : ')
    incrementalChar(ciphertext)

elif(alphabet == "all"):
    print('The 128 different combinations are : ')
    incrementalASCII(ciphertext)
    
else:
    sys.exit("Wrong alphabet given ! Alphabets include dec, alpha, all")
        

        