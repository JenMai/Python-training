'''Suppose you want to generate a random integer between 1 and 10 (1 and
10 both included), but from the random module you only have the random() function
available. How do you do that?'''
from random import random

print( round( random( ) * 10 ) ) # random gives a float between (0.0, 1], rounded to the lowest ten.