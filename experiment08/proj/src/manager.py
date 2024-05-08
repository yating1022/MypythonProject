"""
manager - 

Author: 水果捞
Date: 2024/5/8
Github: https://github.com/yating1022
"""
from proj.config.settings import techer_file
from proj.src.my_pickle import MyPickle
from proj.src.teacher import Teacher


class Manager:
    info = [('查看教师',"show_teacher"),('创建教师','create_teacher'),('删除教师',"delete_teacher"),("推出",'exit')]
    def __init__(self):
        self.techer_pickle_obj = MyPickle(techer_file)
    def show(self,pickle_obj):
        pick_obj = getattr(self,pickle_obj)
        data_info = pick_obj.readiter()
        for teacher_obj in data_info:
            for key in teacher_obj.__dict__:
                print(key,teacher_obj.__dict__[key])
            print('-'*50)
    def show_teacher(self):
        print("教师信息".center(45,'-'))
        self.show('teacher_pickle_obj')
    def create_teacher(self):
        name = input("输入教师姓名").strip()
        eduname = input("请输入教师所在学校名称").strip()
        teacher = Teacher(name,eduname)
        self.teacher_pickle_obj.write(teacher)
        print("教师创建成功")
    def delete_teacher(self):
        self.show_teacher()
        teachername = input("输入删除的教师姓名").strip()
        self.teacher_pickle_obj.delete(teachername)
        print("删除教师成功")
    def exit(self):
        exit()
