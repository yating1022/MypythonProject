import random;
def main():
    list = [1,2,3,5,6,7,8]
    print(random.choice(list))
    print(random.random())
    random.seed(10)
    i = random.random()
    print(i)
    random.seed(10)
    h = random.random()
    print(h)
if __name__ == '__main__':
    main()