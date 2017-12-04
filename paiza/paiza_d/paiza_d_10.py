def main():


    m, n = list(map(int, input().split(" ")))

    if not 1 <= n < m <= 100:
        quit()

    print(m-n)

if __name__ == '__main__':
    main()
