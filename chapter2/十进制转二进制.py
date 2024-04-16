def main():
    number = int(input("输入十进制数"))
    resu  = []
    str = ""
    while number != 0:
        temp = number % 2
        resu.append(temp)
        number = number // 2
    resu.reverse()
    print(resu)
if __name__ == '__main__':
    main()