def main():

    str1 = input()
    str2 = ""
    d = dict({("A",4),("E",3),("G",6),("I",1),("O",0),("S",5),("Z",2)})

    for char in str1:
        if char in d:
            char = d[char]

        str2 = str2 + str(char)

    print(str2)
    
if __name__ == "__main__":
    main()
