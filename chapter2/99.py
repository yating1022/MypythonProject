def main():
    for i in range(1,10,1):
        for j in range(1,i+1,1):
            print("{} * {} = {}".format(i,j,i*j),end="   ",sep=" ")
        print("\n")
if __name__ == '__main__':
    main()