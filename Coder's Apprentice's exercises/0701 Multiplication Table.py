'''Write a program that lets the user enter a number. Then the program displays
the multiplication table for that number from 1 to 10. E.g., when the user enters 12,
the first line printed is “1 * 12 = 12” and the last line printed is “10 * 12 = 120”.'''

from pcinput import getInteger

multiplicand = getInteger( "Please enter a number: " )

#------------------
# Exercise made both with a for and a while loop.
#------------------

for multiplier in range(1,11):
	print("{:>2} * {:>2} = {:>2}".format(multiplier, multiplicand, multiplier*multiplicand))

print()

i = 0
while i <= 10 :
	print("{:>2} * {:>2} = {:>2}".format(i, multiplicand, i*multiplicand))
	i += 1