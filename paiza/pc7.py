price_d = dict({0:5,1:3,2:2,3:1})

def main():

    total_num = int(input())
    point = 0
    scores = [0 for i in range(len(price_d))]

    for _ in range(total_num):
        score = list(map(int, input().split(" ")))
        scores[score[0]] = scores[score[0]] + score[1]

    for itemi, price in enumerate(scores):
        point = point + price_d[itemi] * int(price / 100)

    print(point)

if __name__ == "__main__":
    main()
