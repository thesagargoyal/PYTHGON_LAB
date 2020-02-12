lis = [1,2,3,4,5,6]
lis1 = []

for item in lis :
	if item not in lis1 :
	    lis1.append(item)
	
print(*lis1, sep="*")
