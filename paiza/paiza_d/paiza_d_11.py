def main():

    scorel = list(map(int, input().split(" ")))

    for i in scorel:
        if type(i) is not int:
            raise InvalidArgumentError

    ave = sum(scorel) / len(scorel)

    print(round(ave,1))


if __name__ == '__main__':
    main()
