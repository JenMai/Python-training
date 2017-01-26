'''Ask the user to supply a string. Print how many different vowels there
are in the string. The capital version of a lower case vowel is considered to be the same
vowel. y is not considered a vowel. Try to print nice output (e.g., printing “There are 1
different vowels in the string” is ugly). Example: When the user enters the string “It’s Owl
Stretching Time,” the program should say that there are 3 different vowels in the string.'''

from pcinput import getString

sentence = getString( "Please type something: " ).lower()    # lowering everything makes the process easier.
v = 0

#-------------
# Unless if-statements were in a loop, they return true (or v+1) once that char is met for the first time, and do not iterate.
#-------------

if "a" in sentence :
	v += 1
if "e" in sentence :
	v += 1
if "i" in sentence :
	v += 1
if "o" in sentence :
	v += 1
if "u" in sentence :
	v += 1

if v == 1 :
	print( "There is only one vowel in the string." )
elif v > 1 :
	print( "There are", v, "different vowels in the string." )
else :
	print( "This string has no vowel." )

