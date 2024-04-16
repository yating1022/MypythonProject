def main():
    # 用较大的数除以较小的数，得到余数。
    # 用除数继续除以余数，得到新的余数。
    # 不断重复上述步骤，直到余数为0。
    # 此时，除数即为两个数的最大公约数。例如，对于3139和2117，其最大公约数是73
    # （因为3139除以2117的余数是1022，而2117除以1022的余数是73，且73是唯一能整除1022的数）。
    number1 = int(input("请输入第1个数值"))
    number2 = int(input("请输入第2个数值"))
    if(number1 > number2):
        rem = number1 % number2
        div = number2
        while rem != 0:
            temp = rem
            rem = div % rem
            div = temp
        print("最大公约数是{}".format(div))
    else:
        rem = number2 % number1
        div = number1
        while rem != 0:
            temp = rem
            rem = div % rem
            div = temp
        print("最大公约数是{}".format(div))
    i = (number1*number2)/div
    print("最小公倍数是{}".format(i))
if __name__ == '__main__':
    main()