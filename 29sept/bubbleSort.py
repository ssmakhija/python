'''Bubble Sort'''

def bubbleSort(l1):
    i = 0
    while i < len(l1):
        j = 0
        while j < len(l1) - i - 1:
            if l1[j] > l1[j+1]:
                x = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = x
            j += 1
        i += 1
    return l1

def main():
	l1=[5,1,9,11,3,16,6]
	print(bubbleSort(l1))

if __name__ == '__main__':
	main()