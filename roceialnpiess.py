lis = [1, 1, 2, 2, 3, 4]
lis1 = []

for item in lis :
	if item not in lis1 :
	    lis1.append(item)
	
for item in lis1 :
    print(item,end=" ")
