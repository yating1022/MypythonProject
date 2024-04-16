a=['ok','123',12,False]
a.append(100)
a.append([1,2])
a.extend([3,4])
a.extend([8])
a.insert(1,'inset')
del a[0]
i = a.index('inset')
print(a)
print(i)