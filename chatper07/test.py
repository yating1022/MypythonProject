import os
import sys
import socket
import time


def add_log(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        now_time = time.ctime()
        hostname = socket.gethostname()
        process_full_name = sys.argv[0]
        print(process_full_name)
        process_name=os.path.split(process_full_name)[-1]
        info = '\n[%s]函数运行的结果是%s'%(fun.__name__,result)
        log = ' '.join([now_time,hostname,process_name,info])
        with open('log.txt','a') as fp:
            fp.write(log)
        fp.close()
        print(log)
        return result
    return wrapper


@add_log
def muisic():
    time.sleep(1)
    print("正在听音乐")
@add_log
def add(x,y):
    return x +y

def main():
    muisic()
    add(5,8)
if __name__ == '__main__':
    main()