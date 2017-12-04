def main():
    m, n = map(int, input().split(" "))

    point = n - m
    if point >= 0:
        print(point)
    else:
        print("No")

if __name__ == '__main__':
    main()
