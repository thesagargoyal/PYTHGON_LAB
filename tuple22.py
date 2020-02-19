lis =[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l = []
lis2=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

for item in lis:
    c=len(item)
    if c==0:
        lis2.remove(item)
print(lis2)
