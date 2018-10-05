'''turn on bits at a specific positon'''

def toggle(no, pos, bits):
	x=(1<<bits)-1
	x=x<<(pos-bits)
	print (no^x)

def main():
	no=eval(input("Enter Number"))
	pos=eval(input("Enter Position"))
	bits=eval(input("Enter Bit"))
	toggle(no, pos, bits)

if __name__ == '__main__':
	main()