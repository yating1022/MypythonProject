import random
def main():
    a= [random.randint(1,100) for x in range(10)]
    b = a [:5]
    c = a[5:]
    b.sort(reverse=True)
    c.sort()
    print(b)
    print(c)
if __name__ == '__main__':
    main()