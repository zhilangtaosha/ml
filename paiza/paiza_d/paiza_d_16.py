def main():
    password = input()
    password_set = set(list(password))
    if len(password_set) == 1:
        print("NG")
    else:
        print("OK")
        
if __name__ == '__main__':
    main()
