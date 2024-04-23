"""
An02sys -

Author: leting130
Date: 2024/4/23
github:https://github.com/yating1022
"""
import subprocess
import time
def startandendtime(fun):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        fun(*args, **kwargs)
        end = time.perf_counter()
        print("运行时间", end - start,'秒')

    return wrapper
@startandendtime
def ping(net, start=1, end=16, n=1, w=1):
    str2 = "icmp_seq"
    iplist = ''
    for x in range(start, end+1):
        ip = net + '.' + str(x)
        command = ["ping", ip, "-c", str(n), "-w", str(w)]
        print(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.decode('utf-8')

        if str2 in output:
            print(ip, "通")
            iplist += ip + '\n'
        else:
            print(ip, "不通")
        print(iplist)
    with open('ip.txt', 'w') as f:
        f.writelines(iplist)
def main():
    ping("192.168.2")

if __name__ == '__main__':
    main()
