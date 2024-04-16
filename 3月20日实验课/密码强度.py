def main():
    while True:
        try:
            password = input("输入你的密码")
            assert len(password) >= 6
            break
        except:
            print("输入的密码小于6位")
    ifstrong= {1:"强度弱",2:"强度偏弱",3:"强度中等",4:"强度偏强",5:"强度强"}
    tf = [False]*5
    for i in password:
        if not tf[0] and i.isdigit():
            tf[0] = True
        elif not  tf[1]  and i.islower():
            tf[1] =  True
        elif not tf[2] and i.isupper():
            tf[2] =True
        elif not tf[3]  and i == '_':
            tf[3] =  True
        elif not tf[4] and i in "!@#%^&*()":
            tf[4] = True
    print("密码强度{}".format(ifstrong[tf.count(True)]))
if __name__ == '__main__':
    main()
