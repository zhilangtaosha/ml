def main():
    other_time_l = list(map(int, input().split(" ")))
    your_time = int(input())
    rank_i = 1

    for time in other_time_l:
        if time > your_time:
            print(rank_i)
            break
        rank_i += 1


    if other_time_l[-1] < your_time:
        print(rank_i)


if __name__ == "__main__":
    main()
