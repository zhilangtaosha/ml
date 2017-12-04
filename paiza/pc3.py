def main():
    participant_num = int(input())
    total_num = int(participant_num * (participant_num-1) / 2)

    gamelist = []
    for _ in range(total_num):
        gamelist.append(list(map(int, input().split(" "))))

    score = [["-" for i in range(participant_num)] for j in range(participant_num)]

    for game in gamelist:
        score[game[0]-1][game[1]-1] = "W"
        score[game[1]-1][game[0]-1] = "L"

    for line in score:
        print(" ".join(line))

if __name__ == '__main__':
    main()
