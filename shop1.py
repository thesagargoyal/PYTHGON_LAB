b = list()
a = "Yes"
while(a=="Yes") :
	c=input()
	b.append(c)
	print("You want to continue shopping")
	a=input()
b.sort(reverse=True, key=len)
print(b)
