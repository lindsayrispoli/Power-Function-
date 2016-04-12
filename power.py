def power_function(base, exponent): #define the function
	""" Takes a base and multiplies by an exponent """

	#terminating case
	if exponent == 0:
		return 1 
	#recursive call
	result = base * power_function(base, exponent - 1)
	
	return result #return the rest 

	


