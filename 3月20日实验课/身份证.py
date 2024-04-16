def main():
    while True:
        number = input("输入身份证号码输入-1时退出")
        numberlist = tuple(number)
        checklist = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
        if number == '-1':
            break
        elif len(number) == 18:
            sum = 0
            for i in range(17):
                wei = int(numberlist[i]) * checklist[i]
                sum += wei
            r = sum%11
            chece = ['1','0','X','9','8','7','6','5','4','3','2']
            if numberlist[len(numberlist)-1] == chece[r]:
                print("{}校验通过".format(number))
            else :
                print("{}校验不通过".format(number))
        else:
            print("你输入的不是一个18位身份证号码")
if __name__ == '__main__':
    main()