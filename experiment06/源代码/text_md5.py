"""
text_md5 - 

Author: leting130
Date: 2024/4/22
github:https://github.com/yating1022
"""
import hashlib
def qiepian(size,text):
    start = 0
    while start < len(text):
        qie = text[start:start+size]
        yield qie
        start = start + size
    return
def main():
    text = input("输入长文本进行加密")
    text_passwds = []
    hash= hashlib.md5()
    for row in qiepian(64,text.encode('utf-8')):
        hash.update(row)
        text_passwd = hash.hexdigest()
        text_passwds.append(text_passwd)
    print('加密结果')
    for x in text_passwds:
        print(x)
if __name__ == '__main__':
    main()