"""
isRegister - 

Author: leting130
Date: 2024/4/22
github:https://github.com/yating1022
"""
import json


def main():
    with open("user_json.json", 'r', encoding="utf-8") as f:
        user_data = json.load(f)
        while True:
            user = input("请输入用户名")
            if user in user_data:
                print(user,"用户已存在")
            else:
                password = input("输入密码")
                user_data[user] = password
                with open("user_json.json", 'w', encoding="utf-8") as f:
                    json.dump(user_data,f,ensure_ascii=False)
                ifdo = input("是否退出，Y/y退出")
                if ifdo in "Yy":
                    return
if __name__ == '__main__':
    main()