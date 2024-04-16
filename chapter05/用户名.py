def main():
    users = {}
    while  True:
        print('菜单'.center(32,'*'))
        print("0：退出".center(32,'*'))
        print("1：添加用户".center(31,'*'))
        print("2：删除用户".center(31,'*'))
        print("3：修改用户".center(31,'*'))
        print("4：查询用户".center(31,'*'))
        print("".center(34,'*'))
        cmd = eval(input("输入操作:"))
        if cmd == 1:
            name = input("请输入用户名：")
            if name in users.keys():
                input("该用户已经存在")
                continue
            password = input("请输入密码")
            users[name] = password
            print("添加完成".center(33,'*'))
            iftodo = input("添加完成是否继续添加,y of Y 继续")
            if iftodo in 'yY':
                continue
            else:
                break
        if cmd == 4:
            for key, value in users.items():
                print(key.center(31, '*'))
            continue
        if cmd == 2:
            delname = input("输入要删除的用户")
            if delname in users.keys():
                del users[delname]
                continue
            else:
                print("不存在该用户")
                continue
        if cmd == 3:
            rename = input("输入要修改的用户")
            if rename in users.keys():
                users[rename] = input("输入新的密码")
            else:
                print("用户不存在")
                continue
        else:
            break
if __name__ == '__main__':
    main()