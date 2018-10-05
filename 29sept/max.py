'''WAPTA List of integers from user and return max and second max integer from it. (Without using inbuilt functions)'''

def max(l1):
	if l1==None:
		return
	elif len(l1)==1:
		return l1[0], None
	else:
		max=l1[0]
		smax=l1[1]
		if smax>max:
			max=l1[1]
			smax=l1[0]
		for x in l1[2:]:
			if x>max:
				smax=max
				max=x
			elif x>smax:
				smax=x
	print("Given List is:")
	print(l1)
	print("Max and Second Max is:")
	print(max, smax)

def main():
	l1=[1, 2, 3, 5, 1, 2, 7, 1, 2]
	max(l1)

if __name__ == '__main__':
	main()