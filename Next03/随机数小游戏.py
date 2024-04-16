import random
def main():
    input("按下回车生成随机数,开始小游戏")
    i = random.randrange(0,100,1)
    while True:
        n = int(input("输入猜测的数值"))
        if n > i :
            print("您输入的数值太大了")
        elif n < i :
            print("您输入的数值太小了")
        else:
            print("您答对啦,答案为{}".format(n))
            break
if __name__ == '__main__':
    main()