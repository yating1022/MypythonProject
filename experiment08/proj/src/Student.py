"""
Student - 

Author: 水果捞
Date: 2024/5/8
Github: https://github.com/yating1022
"""
class Student:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
    def print(self):
        return self.name + " " + str(self.age) + " " + self.count
def main():
    s1 = Student("tom",20)
    s2 = Student("losi",90)
    s3 = Student("jack",80)
    s4 = Student("lucy",70)
    print("学生个数：{0}".format(Student.count))
if __name__ == '__main__':
    main()