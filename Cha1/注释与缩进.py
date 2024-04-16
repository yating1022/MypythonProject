# 单行注释为#
'''
多行注释
为三个成对的单引号
'''
# 当在一行的最后加上\就与下一行形成逻辑行，与docker相同,如:
def main():
    i = int\
    (input("输入i"))
    print(i)
if __name__ == '__main__':
    main()