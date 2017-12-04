def main():
    total_player_num = int(input())
    players = list(map(int, input().split(" ")))

    d = dict({})
    for player in players:
        if player in d:
            d[player] += 1
        else:
            d[player] = 1

    max_val = max(d.values())
    max_player_list = [key for key in d if d[key] == max_val]

    print(" ".join(map(str,sorted(max_player_list))))

if __name__ == '__main__':
    main()
