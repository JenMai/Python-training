'''The Pythagorean theorem states that of a right triangle, the square of the
length of the diagonal side is equal to the sum of the squares of the lengths of the other
two sides (or a2 + b2 = c2). Write a program that asks the user for the lengths of the two
sides that meet at a right angle, then calculate the length of the third side, and display it
in a nicely formatted way. You may ignore the fact that the user can enter negative or zero
lengths for the sides.'''

from pcinput import getFloat
from math import sqrt

while True :
	a = getFloat( "Length of the first side: " )
	b = getFloat( "Length of the second side: " )
	
	if ( a <= 0 ) or ( b <= 0) :
		print( "This is not a valid right triangle." )
		continue
		
	else:
		break

c = sqrt(a**2 + b**2)

print( "Length of the hypotenuse is {:.2f}.".format( c ) )

