def main():

    temp, humid = map(int, input().split(" "))

    if 25 <= temp or humid <= 40:
        if 25 <= temp and humid <= 40:
            print("No")
        else:
            print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
