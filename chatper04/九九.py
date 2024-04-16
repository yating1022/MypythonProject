list = [str(x)+"*" + str(y) +'='+ str(x*y)+ ('\n' if x == y else ' ')
        for x in range(1,10)
            for y in range(1,x+1)]
for i in list:
    print(i,end=' ')
