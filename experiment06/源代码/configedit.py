"""
configedit - 

Author: leting130
Date: 2024/4/22
github:https://github.com/yating1022
"""
import configparser
def main():
    myconfig = configparser.ConfigParser()
    myconfig.read("config.ini")
    string = myconfig.sections()
    print(string)
    if myconfig.has_section("database"):
        items = myconfig.items("database")
        print(items)
        values = myconfig.get("database","port")
        print("port为"+values)
        has_encoding = myconfig.has_option("database","encoding")
        print(has_encoding)
        if has_encoding:
            myconfig.remove_option("database","encoding")
            myconfig.write(open('../config.ini', 'w'))
        else:
            myconfig.set("database","encoding","utf-8")
            myconfig.write(open('../config.ini', 'w'))
    else:
        myconfig["database"] = {"host": "127.0.0.1", "user": "root", "password": "123", "port": 3306, "db": "pet"}
if __name__ == '__main__':
    main()