'''The Fibonacci sequence is a sequence of numbers that starts with 1, followed
by 1 again. Every next number is the sum of the two previous numbers. I.e., the sequence
starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a program that calculates and prints the Fibonacci
sequence until the numbers get higher than 1000.'''

x = 1
y = 1
z = 0

print( x, y, end =" " )

while True :
	z = x+y				# sum of the previous two numbers
	x = y				# first previous number's variable is switched to second
	y = z 				# second previous number's variable is switched to sum
	print(z, end =" " )
	if z > 1000 : 
		break 
