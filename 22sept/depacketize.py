def DePacketize(packet):
	data=packet&((1<<15)-1)
	packet=packet>>15
	len=packet&((1<<9)-1)
	packet=packet>>9
	flag=packet&1
	packet=packet>>1
	crc=packet&((1<<7)-1)

	print (crc, flag, len, data)

def main():
	packet=992510975
	DePacketize(packet)

if __name__ == '__main__':
	main()