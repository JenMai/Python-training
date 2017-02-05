#-----------------------------------------------
# loop until user doesn't want to play anymore (not a really elegant way to do so, admittedly!):
#-----------------------------------------------
while True :
    #-----------------------------------------------
    # loop until user write a legal input:
    #-----------------------------------------------
	while True :													
		try :
			input_sec = int(raw_input("Enter the seconds you want to convert: ")) 	# turns string from raw_input into an integer
		except ValueError :															# when input can be turned into an integer
			print "Sorry, I don't understand, please enter a positive integer (>0) :(."
			continue 																# inner while loop starts over

		if input_sec < 0 :															# negative int can't be converted
			print "Sorry, integer must be positive (>0)."
			continue 

		if input_sec <= 59 :														# no need to convert
			print str(input_sec) + " second(s)."
			continue 
		else :
			break 																	# when input is an integer > 59, break the loop
	 
    #-----------------------------------------------
    # functions to get time in minutes/seconds/hours :
    #-----------------------------------------------
	def get_min(time) :
		min = (time/60)%60 															# result must stay between 0 and 59.
		if min >= 0 :
			return min

	def get_sec(time) :
		sec = time%60 																# result must stay between 0 and 59.
		if sec >= 0 :
			return sec

	def get_hour(time) :
		hour = time/3600
		if hour >= 0 :
			return hour
			
	print str(get_hour(input_sec)) + " hour(s), " + str(get_min(input_sec)) + " minute(s) and " + str(get_sec(input_sec)) + " second(s)."
	
    #-----------------------------------------------
    # determine if user wants to play again
    #-----------------------------------------------
	yes_no = raw_input("Try again ? (y/n)").lower()
	if (yes_no == "y"):
		continue 																	# starts over
	elif (yes_no == "n"):
		break 																		# program ends
	else :
		print "I don't understand."
		break
