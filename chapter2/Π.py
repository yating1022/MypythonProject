def main():
    n = 3
    pai = 1
    while n < 10000000:
        if((n - 1) / 2 )%2 ==0:
            pai += 1/n
        else:
            pai -= 1/n
        n += 2
    print(4*pai)
if __name__ == '__main__':
    main()