'''Write a function customIndex() which returns list of indices where the given data is present in the input list.'''
def customIndex(l1, data):
	result=[]
	count=l1.count(data)
	prev_index=0
	while count!=0:
		index=l1[prev_index:].index(data)
		result.append(index+prev_index)
		count-=1
		prev_index=index+1+prev_index
	print(result)

def main():
	l1=[1, 2, 3, 5, 1, 2, 7, 1, 2]
	data=eval(input("Enter Number to Search Index"))
	customIndex(l1, data)

if __name__ == '__main__':
	main()