import datetime
import time


def warning():
    print("现在应该打卡了")
def main(hour = 0 ,minte = 0):
    while True:
        while True:
            nowtime = datetime.datetime.now()
            if nowtime.hour == hour and nowtime.minute ==minte:
                break
            else:
                time.sleep(60)
        warning()
if __name__ == '__main__':
    main(9,1)

