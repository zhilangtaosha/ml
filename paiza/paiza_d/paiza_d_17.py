def main():

    str = input()

    if "False" in str:
        print(str.replace("False","True"))
    else:
        print(str)

if __name__ == "__main__":
    main()
