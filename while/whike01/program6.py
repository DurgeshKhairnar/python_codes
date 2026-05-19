# write a program to print only consonant alphabets for A to Z but must not be any vowels in  the output.

alphabet = 65

while alphabet >= 65 and  alphabet < 91 :
    char = chr(alphabet)
    if char != "A" and char != "E" and char != "I" and char != "O" and char != "U" :
        print(char, end = " ")
    alphabet += 1
