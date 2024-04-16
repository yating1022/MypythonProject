login1 = 0

def iflogin(func):
    def loginui(*args, **kwargs):
        global login1  # 声明全局变量以在函数内部进行修改
        if login1 == 1:
            return func(*args, **kwargs)  # 如果已登录，直接调用被装饰的函数
        else:
            print("未登录")
            user = input("输入账号: ")
            password = input("输入密码: ")
            if user == "admin" and password == "123456":
                login1 = 1  # 登录成功，修改登录状态
                return func(*args, **kwargs)  # 调用被装饰的函数
            else:
                print("账号或密码错误")

    return loginui

@iflogin
def ui():
    while True:
        print("1.homepage".center(35, '*'))
        print("2.clothingpage".center(35, '*'))
        print("3.bookpage".center(35, '*'))
        print("4.gameoage".center(35, '*'))
        doui = int(input("输入要进入的页面"))
# 测试装饰后的函数
ui()
