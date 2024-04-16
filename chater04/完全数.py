import datetime
import time


def main():
    resu = []
    stattime = time.time()
    for i in range(2,1000):
        for n in range(1,i//2+1):
            if i % n == 0 :
                resu.append(n)
        if i == sum(resu):
            print(i,"是完全数，真因子为",resu)
        resu = []
    end = time.time()
    print("用时",end - stattime)
if __name__ == '__main__':
    main()
