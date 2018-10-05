def Packetize(crc, flag, len, data):
	packet=crc&127
	packet=packet<<1
	packet=packet|(flag&1)
	packet=packet<<9
	packet=packet|(len&511)
	packet=packet<<15
	packet=packet|(data&(32767))
	print (packet)

def main():
	crc=29
	flag=1
	len=81
	data=1023
	Packetize(crc,flag, len, data)

if __name__ == '__main__':
	main()