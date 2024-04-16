def main():
    number = int(input("输入十进制数"))
    while True:
        try:
            n = int(input("输入要转换的进制 2或者8"))
            assert n == 2 or n == 8
            break
        except:
            print("你输入的进制有误")
    resu  = []
    str = ""
    while number != 0:
        temp = number % n
        resu.append(temp)
        number = number // n
    resu.reverse()
    print(resu)
if __name__ == '__main__':
    main()