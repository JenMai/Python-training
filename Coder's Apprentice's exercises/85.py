'''Write a program that processes a collection of numbers using a for loop. The
program should end immediately, printing only the word “Done,” when a zero is encountered
(use a break for this). Negative numbers should be ignored (use a continue for this;
I know you can also do this with a condition, but I want you to practice with continue).
If no zero is encountered, the program should display the sum of all numbers (do this in
an else clause). Always display “Done” at the end of the program. Test your program
with the collection ( 12, 4, 3, 33, -2, -5, 7, 0, 22, 4 ). With these numbers, the
program should display only “Done.” If you remove the zero, it should display 85 (and
“Done”).'''

total = 0

for num in ( 12, 0, 4, 3, 33, -2, -5, 7, 22, 4 ) :
	if num < 0 :
		continue

	if num == 0 :
		break
	
	else:	
		total += num
		continue

if total == 85 : 
	print( total )
print( "Done" )