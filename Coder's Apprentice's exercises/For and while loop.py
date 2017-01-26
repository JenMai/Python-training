def getInteger( prompt ):
    while True:
        try:
            num = int( input( prompt ) )
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num
 
# ---------------------------------------------------------------------------
# syntax for a for loop:
# ---------------------------------------------------------------------------
print( "for loop: " )
total = 0
 
for typed_num in range( 1,6 ) :                                                 # typed_num will take a value between 1 and 5 included.
    num = getInteger( " Please write down number {}: ".format( typed_num ) )
    total += num                                                                # adds each value entered in the loop.
 
print( total )
 
# ---------------------------------------------------------------------------
# syntax for a while loop:
# ---------------------------------------------------------------------------
print( "while loop: " )                                                         # variables take new values :
typed_num = 1                                                                   # A way to avoid "write down number 0"
total = 0                                                                       # total takes a 0 back.
 
while typed_num <= 5 :
    num = getInteger( " Please write down number {}: ".format( typed_num ) )
    total += num                                                                # adds each value entered in the loop.
    typed_num += 1                                                              #prevent infinite loop
 
print( total )