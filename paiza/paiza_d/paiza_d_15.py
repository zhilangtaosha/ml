def main():
    num = input()
    l = list(map(int, num))
    if l[0] == 4:
        print('error')
    elif l[0] == 2:
        print('ok')
    else:
        print('unknown')

if __name__ == '__main__':
    main()
