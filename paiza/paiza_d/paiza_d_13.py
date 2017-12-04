def main():
     num = int(input())

     if not 1 <= num <= 100:
        quite()

     if num % 2 == 0:
         print('OFF')
     else:
        print('ON')

if __name__ == '__main__':
    main()
