'''Ask the user to enter three numbers. Then print the largest, the smallest,
and their average, rounded to 2 decimals.'''
from pcinput import getFloat

num1 = getFloat( "Insert a first number: " )
num2 = getFloat( "Insert a second number: " )
num3 = getFloat( "Insert a third number: " )

min_input = min(num1, num2, num3)
max_input = max(num1, num2, num3)
average_min_max = (min_input + max_input) / 2

print( "The largest number is ", max_input)
print( "The smallest number is ", min_input)
print( "Their average is", round(average_min_max, 2))