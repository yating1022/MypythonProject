import random
def main():
    list = [1,2,3,4,5,6,7]
    print("原始的list:",list)
    random.shuffle(list)
    print("随机打乱后的list:",list)
if __name__ == '__main__':
    main()