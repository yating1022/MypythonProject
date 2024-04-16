def main():
    number1 = int(input("输入第1个数字："))
    number2 = int(input("输入第2个数字："))
    if number1 < number2:
        print("number1=number2")
    elif number1 == number2:
        print("number1 = number2")
    else:
        print("number2< number1")
if __name__ == '__main__':
    main()