"""
main - 

Author: 水果捞
Date: 2024/5/8
Github: https://github.com/yating1022
"""
from proj.src.manager import Manager
def main():
    mana = Manager.info
    for x in range(len(mana)):
        print(x+1,mana[x][0])
    while True:
        ch = input("请输入序号：").strip()
        # getattr(对象，对象属性) 返回一个对象属性值
        getattr(Manager(),mana[int(ch)-1][1])#反射