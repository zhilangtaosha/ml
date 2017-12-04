# C041
from operator import itemgetter
def main():

    total_num = int(input())
    scores = []

    for _ in range(total_num):
        score = list(map(int, input().split(" ")))
        scores.append(score)

    scores.sort(key=itemgetter(0,1,2), reverse=True)

    for score in scores:
        print(" ".join(map(str,score)))

if __name__ == "__main__":
    main()
