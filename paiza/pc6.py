def main():
    l = list(input().split("+"))

    total = 0

    for l_str in l:
        total = total + l_str.count("/") * 1 + l_str.count("<") * 10

    print(total)

if __name__ == "__main__":
    main()
