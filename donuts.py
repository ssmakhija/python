x=eval(input("Enter 1 Number"))
if x<1:
	print("invalid input")
elif x<=2:
	print("too few donuts")
elif x<11:
	print("Number of Donuts "+str(x))
else:
	print("No of donuts too many")
