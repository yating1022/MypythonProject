def main():
    for i in range(100):
        ifsu = True
        for j in range (2,i):
            if i % j == 0:
                ifsu = False
        if ifsu:
            print(i)
if __name__ == '__main__':
    main()

