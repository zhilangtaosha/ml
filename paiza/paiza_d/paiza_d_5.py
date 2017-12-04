def main():
    
    time = int(input())
    
    if not 0 <= time <= 47:
        print("Pls check values")
        quit()
    
    print(time%24)
    
if __name__ == '__main__':
    main()