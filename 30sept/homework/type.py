l= []
data = ''
no=eval(input("Enter Number of items in list"))
for i in range(no):
    data=eval(input("Enter Data for list"))
    l.append(data)

for i in l:
    print (i, type(i)) 

