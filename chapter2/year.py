def main():
    year = int(input("请输入需要判定的年份"))
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        print("这是一个闰年哦")
    else:
        print("你输入的不是一个闰年")
if __name__ == '__main__':
    main()