total = 0
x = 1
grade = 0 

#-------------------------------------------------------
# function used to get a floating number from user; from The Coder's Apprentice: http://www.spronck.net/pythonbook/
#-------------------------------------------------------
def getFloat( prompt ):
    while True:
        try:
            num = float( input( prompt ) )
        except ValueError:
            print( "That is not a gradeber -- please try again" )
            continue
        return num


print( "Enter your grades, out of 20." )
print( "Please type '-1' once you're done." )

#-------------------------------------------------------
# loop-and-a-half to get every grade user wants to input:
#-------------------------------------------------------
while True :
    grade = getFloat( "Please enter grade num. {}: ".format( x ) )    # x indicates how many grades entered so far
    if (grade < -1) or (grade > 20) :
        print( "Grade must be between 0 and 20" )                     # -1 still need to be off that if-statement as it's used to end the loop
        continue                                                      # doesn't consider input if one condition is True, loop starts over
    if grade == -1 : 
        break                                                         # break when user is done.
    total += grade                                                    # accumulating inputs to the total if other if-statements are False
    x+=1

average = total / (x-1)                                               # average score once loop is broken, minus change in x when input is -1

print( "Total is", total )
print( "average is", average )

#-------------------------------------------------------
# conversion to the American score (kind of, not GPA though) :
#-------------------------------------------------------
if average >= 17 :
    print( "In America, your score would be an A! Congratulations!")
elif (average >= 15) and (average < 17) :
    print( "In America, your score would be a B!")
elif (average >= 13) and (average < 15) :
    print( "In America, your score would be a C!" )
elif (average >= 11) and (average < 13) :
    print( "In America, your score would be a D!" )
else:
    print( "In America, your score would be an F!" )