import time

namelist = ['郭靖', '黄蓉', '令狐冲', '张无忌', '杨过', '韦小宝', '小龙女']
time_format1 = '%Y-%m-%d'  # 时间格式1
time_format2 = '%H:%M:%S'  # 时间格式2

while True:
    userIndex = int(input("请输入员工序号（1-7）打卡，输入0退出"))
    if userIndex == 0:
        break
    current_time = time.localtime()
    time_str = time.strftime(time_format2, current_time)
    employee_name = namelist[userIndex - 1]
    hour = int(time.strftime("%H", current_time))
    if hour < 10:
        state = "打卡成功"
    else:
        state = "打卡失败"
    print("{} {} {}".format(employee_name, time_str, state))
