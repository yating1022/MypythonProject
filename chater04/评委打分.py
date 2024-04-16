import copy
def main():
    while True:
        number = int(input("请输入评委的人数"))
        try:
            if number <= 2 :
                print("评委必须多于2人")
            else:
                break
        except:
            pass
    resr = []
    for i in range(number):
        while True:
            try:
                scor = float(input("请输入第{}个评委的分数".format(i+1)))
                assert 0.0 <= scor <= 10.0
                resr.append(scor)
                break
            except:
                print("你输入的分数有误")
    maxsocr = max(resr)
    minscor = min(resr)
    resr1 = copy.deepcopy(resr)
    resr.remove(maxsocr)
    resr.remove(minscor)
    avgscor = sum(resr)/(number-2)
    avgscor1 = sum(resr1)/number
    print("评委打的原始分".center(60,'='),'\n',resr1)
    print("去掉最低最高分".center(60,'='),'\n',resr)
    print("原始获得的分数".center(60,'='),'\n',avgscor1)
    print("最终获得的分数".center(60,'='),'\n',avgscor)
if __name__ == '__main__':
    main()

