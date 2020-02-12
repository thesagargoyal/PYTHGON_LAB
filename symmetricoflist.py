lis = [1,2,3,4,5,6]
lis1 = [1,2,3,4,8,9]

lis2=[i for i in lis if i not in lis1]
lis3=[j for j in lis1 if j not in lis]
lis4=lis2+lis3
print(lis4)


