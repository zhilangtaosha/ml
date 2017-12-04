def main():

    n = int(input())
    temp = input()
    s_count = 0
    r_count = 0

    if len(temp) is not n:
        quit()

    for t in temp:
        if t is 'S':
            s_count += 1
        else:
            r_count += 1

    print(str(s_count) + " " +str(r_count))

if __name__ == '__main__':
    main()
