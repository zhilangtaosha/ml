def main():
    other_time_l = list(map(int, input().split(" ")))
    your_time = int(input())
    rank_i = 1

    for i, time in enumerate(other_time_l):
        if time > your_time:
            print(rank_i)
            break

        rank_i += 1

        if len(other_time_l) == i+1:
            print(rank_i)

if __name__ == "__main__":
    main()
