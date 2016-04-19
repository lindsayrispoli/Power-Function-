import power
#---------------------- Main Program --------------------------


def int_input(question):
	''' Ask the user for an int, and let them try again.'''
	
	answer = input(question)
	
	try:
		#terminating case 
		answer = int(answer)
		return answer
	except ValueError:
		#recursive call
		return int_input("That was not an integer;  Try again. ")	

def float_input(question):
	''' Ask the user for an int or float, and let them try again.'''
	
	answer = input(question)
	
	try:
		#terminating case 
		answer = float(answer)
		return answer
	except ValueError:
		#recursive call
		return float_input("That was not an integer;  Try again. ")	

base = float_input("Enter a base: ")
exponent = int_input("Enter an exponent for the base: ")

output = power.power_function(base, exponent)
print(output)


