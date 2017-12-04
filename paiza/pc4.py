# C041
def main():
    total_num = int(input())
    scores = []
    for _ in range(total_num):
        score = list(map(int, input().split(" ")))
        scores.append(score)

    scores.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)

    for score in scores:
        print(" ".join(map(str,score))))

if __name__ == "__main__":
    main()
