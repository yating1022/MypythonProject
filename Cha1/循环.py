def main():
    name = ['张三','李四','王五']
    for onename in name:
        print(onename)
    for nameindex in range(len(name)):
        print(name[nameindex])
    i = 0
    while i <  len(name):
        print("while循环的：{}".format(name[i]))
        i+=1
    for h in range(0,10,3):
        print(h)
if __name__ == '__main__':
    main()