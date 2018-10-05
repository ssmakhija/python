l = [35,53,[525,6743, [541, 54, [125, 45, [56446, 545454, [6666, [65464]]]]]],64,63,[743,754,757]]

def flatten(l):
	result = []
	if isinstance(l, (list)):
		for x in l:
			result.extend(flatten(x))
	else:
		result.append(l)
	return result



x=flatten(l)
for i in x:
	print(i)