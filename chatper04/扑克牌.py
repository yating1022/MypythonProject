#利用元组创建扑克牌A1(A,1)A2(A,2)
#先创建列表
import random
yz1 = ('黑桃','红心','梅花','方块')
yz2 = ('A','1','2','3','4','5','6','7','8','9','10','J','Q','K')
list = []
for x in yz2:
    for y in yz1:
        list.append((x,y))
list.append("大鬼")
list.append("小鬼")
random.shuffle(list)
pkp = tuple(list)
play1=[]
play2=[]
play3=[]
play4=[]
for i in range(0,len(pkp)-1):
    if (i + 1) % 4 == 1:
        play1.append(pkp[i])
    elif (i + 1) % 4 == 2:
        play2.append(pkp[i])
    elif (i + 1) % 4 == 3:
        play3.append(pkp[i])
    elif ( i + 1) % 4 == 0:
        play4.append(pkp[i])
print(play1)
print(play2)
print(play3)
print(play4)