def power_function(base, exponent): #define the function
	""" Takes a base and multiplies by an exponent """
	
	multiply = 0 #Variable tells how many times the base is multiplied
	product = 1 #calculates the final product of the multiplication  

	while multiply < int(exponent):
		product *= int(base) #multiply the product by the base
		multiply += 1 #increase the multiply each time. 
					  #In the end, the value of multiply should be -1 than the exponent 
		
	return product 

#----------------------- Main Program --------------------------

base = input("Enter a base: ")
exponent = input("Enter an exponent for the base: ")

multipliedNumber = power_function(base, exponent) #multipliedNumber should be the calculated product
#could multipliedNumber also be called product?

print("Power(" + str(base) + ", " + str(exponent) + ") --> " + str(multipliedNumber)) 