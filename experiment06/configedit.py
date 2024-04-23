"""
configedit - 

Author: leting130
Date: 2024/4/22
github:https://github.com/yating1022
"""
import configparser
def main():
    myconfig = configparser.ConfigParser()
    print(myconfig.read('myconfig.ini', encoding='utf-8'))
    if myconfig.has_section('database'):
        print(myconfig)
    else:
        myconfig.write('myconfig.ini')
        print(myconfig)
if __name__ == '__main__':
    main()