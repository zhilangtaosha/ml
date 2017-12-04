def main():

    total_player_num = int(input())
    players = sorted(list(map(int, input().split(" "))))

    l = [0 for _ in range(max(players))]

    for pi in players:
        l[pi - 1] += 1

    max_val = max(l)
    max_count = l.count(max_val)

    s = ""

    max_i = 1
    for i in range(max(players)):
        if l[i] == max_val:
            if max_i == max_count:
                s += str(i+1)
            else:
                s += str(i+1) + " "
            max_i +=1
    print(s)

if __name__ == "__main__":
    main()
