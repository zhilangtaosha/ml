def isinteger(x):
    if isinstance(x, int):
        return True
    else:
        print("Input Integer")

def main():

    inputs = input()
    ilist = list(map(int,inputs.split(" ")))
    ia, ib = ilist
    tmp = ia * ib

    if isinteger(tmp) is True:
        if tmp < 9999:
            print(tmp)
        else: 
            print("NG")

if __name__ == '__main__':
    main()
