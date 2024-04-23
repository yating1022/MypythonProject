"""
timetext.py - 

Author: leting130
Date: 2024/4/22
github:https://github.com/yating1022
"""
import time
def main():
    witch = 50
    start = time.perf_counter()
    for x in range(witch +1):
        finished = '*' * x
        unfinished = '.' * (witch-x)
        percent = (x / witch) * 100
        runtime = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}秒".format(percent,finished,unfinished,runtime),end=" ")
        time.sleep(0.1)
    print("执行结束")
if __name__ == '__main__':
    main()
