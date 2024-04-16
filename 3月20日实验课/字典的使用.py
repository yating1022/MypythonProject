name = {"霍元甲": "hyj", "陈真": "cz", "霍东觉": "hdj", "郭嘉": "gj", "郭靖": "gj", "黄蓉": "hr", "东方不败": "dfbb"}
while True:
    user = input("请输入要删除的名字")
    if user in name:
        yn = input("用户存在，是否删除,y删除，其他退出")
        if yn in 'Yy':
            del name[user]
            yn2 = input("删除成功，是否继续删除，Y继续，其他键退出")
            if yn2 in "yY":
                continue
            else:
                break
    else:
        print("该用户不存在，请重新输入")
print("显示用户信息")
print("*" * 35)
print(name)