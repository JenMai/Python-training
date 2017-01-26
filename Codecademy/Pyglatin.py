#-------------------------------------------------------
# loop until user writes alphabetical characters only
#-------------------------------------------------------
while True :
    original = raw_input("Enter a word to convert :").lower()
    if original.isalpha() and (len(original) > 0) :
        break                                                   # if input is made of at least 1 letter, loop ends.
    else:
        print "Please enter letters."                           # if input is made of at least 1 letter, loop ends.
 
FIRST_L = "aeiouy"
 
if original[0] in FIRST_L :
    print original + "ay"                                       #if the first letter is a vowel, it doesn't move
else:
    print original[1:] + original[0] + "ay"                     #returns the word starting its 2nd letter, first letter at the end + ay