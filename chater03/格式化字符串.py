def main():
    str1='hello,world'
    sub = 'o'
    print(str1.count(sub))#count函数统计字符串个数
    str1='厦门'
    str1_utf8 = str1.encode('utf-8')#字符串转换为utf-8编码
    str1_gbk = str1.encode('gbk')#字符串转换为gbk编码
    print(str1_utf8)
    print(str1_gbk)
    print(str1_utf8.decode('utf-8'))#utf-8转换为字符串
    print(str1_gbk.decode('gbk'))#gbk转换为字符串
if __name__ == '__main__':
    main()