def main():
    a = list(get_input()) # [a1, a2, a3, ...]

    print(a)

def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

if __name__ == '__main__':
    main()
