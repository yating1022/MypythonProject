def main():
    hei = int(input("请输入你的体重"))
    ght = int(input("请输入你的身高"))
    bmi = hei / ght
    if bmi < 18.5:
        print("偏瘦")
    elif 18.5 <= bmi < 25:
        print("正常")
    elif 25 <= bmi <30:
        print("偏胖")
    elif bmi>30:
        print("肥胖")
if __name__ == '__main__':
    main()