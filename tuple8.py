to avoid changes in previous tuple just like deepcopy case of list
t=(1,4,[])
d=eval(str(t))
d[-1].append(100)
print(d)
print(t)

