def main():
    yourName = input('输入你的名字：')
    youAge = int(input("输入你的年龄："))
    print("你的名字是{}你的年龄是{}".format(yourName,youAge))
    print(yourName,youAge,sep="分隔符")
    print("你的名字是%s,你的年龄是%d"%(yourName,youAge))
if __name__ == '__main__':
    main()