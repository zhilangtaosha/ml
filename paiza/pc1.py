def strike_counter():
    n = [0]
    def inc():
        n[0] += 1
        return n[0]
    return inc

def ball_counter():
    n = [0]
    def inc():
        n[0] += 1
        return n[0]
    return inc

def main():
    index = int(input())
    counts = []
    for i in range(index):
        count = input()
        counts.append(count)

    strike_count = strike_counter()
    ball_count = ball_counter()

    for count in counts:

        if count == "strike":
            sc = strike_count()
            if sc == 3:
                print("out!")
                break

        elif count == "ball":
            bc = ball_count()
            if bc == 4:
                print("fourball!")
                break
        print(count + "!")

if __name__ == '__main__':
    main()
