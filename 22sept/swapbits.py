'''Swapping Bits'''

def swapbits(no1, no2, pos, bits):
	x=(1<<bits)-1
	x=x<<(pos-bits)

	no1_part=no1&x
	no2_part=no2&x
	no1=no1&~x
	no2=no2&~x
	no1=no1|no2_part
	no2=no2|no1_part

	print (no1, no2)

def main():
	no1=eval(input("Enter number 1"))
	no2=eval(input("Enter number 2"))
	pos=eval(input("Enter position"))
	bits=eval(input("Enter bits"))
	swapbits(no1, no2, pos, bits)

if __name__ == '__main__':
	main()