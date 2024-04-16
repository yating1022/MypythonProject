import random
def main():
    num = int(random.random()*100) + 1
    usernum = int(input("猜一下数字是多少"))
    while num != usernum:
        if usernum > num:
            print("大了")
        else:
            print("小了")
        usernum = int(input("猜一下数字是多少"))
    print("你猜对了")
if __name__ == '__main__':
    main()