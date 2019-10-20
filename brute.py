import sys
from dec import incrementalNumber

if(len(sys.argv) != 3):
    sys.exit("Usage : python3 brute.py <charset> <ciphered_text>")

else:
    print("Alphabet chosen : ", sys.argv[1])
    print("The original ciphered text found is : ", sys.argv[2])

alphabet = sys.argv[1]
ciphertext = sys.argv[2]

if(alphabet == "dec"):
    print('The 10 different combinations are : ')
    incrementalNumber(ciphertext)
elif(alphabet == "alpha"):
    sys.exit()
elif(alphabet == "all"):
    sys.exit()
else:
    sys.exit("Wrong alphabet given ! Alphabets include dec, alpha, all")
        

        