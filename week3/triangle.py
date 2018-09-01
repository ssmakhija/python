x=eval(input("Enter 1st side"))
y=eval(input("Enter 2nd side"))
z=eval(input("Enter 3rd side"))

if (x+y > z) :
	print("Entered Values form triangle")
elif (y+z > x) :
	print("Entered Values form triangle")
elif (z+x >= y) :
	print("Entered Values form triangle")
else:
	print("Entered Values don't form triangle")
