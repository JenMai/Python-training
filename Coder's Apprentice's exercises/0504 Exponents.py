from math import exp

'''Calculate the value of e to the power of -1, 0, 1, 2, and 3, and display the
results, with 5 decimals, in a nicely formatted manner.'''
e = exp( 1 )
s = "e to the power of {:^3d} is {:>5.5f} "

print( s.format( -1, exp( -1 ) ) )
print( s.format( 0, exp( 0 ) ) )
print( s.format( 1, exp( 1 ) ) )
print( s.format( 2, exp( 2 ) ) )
print( s.format( 3, exp( 3 ) ) )
