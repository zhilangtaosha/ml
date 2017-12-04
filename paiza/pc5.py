#C044
def main():

    total_num = int(input())

    jd = dict({})
    for ci in range(total_num):
        j_input = input()
        if j_input not in jd:
            jd[j_input] = 1

    if len(jd) == 3 or len(jd) == 1:
        print("draw")
    elif len(jd) == 2:
        if "paper" not in jd:
            print("rock")
        elif "rock" not in jd:
            print("scissors")
        elif "scissors" not in jd:
            print("paper")

if __name__ == "__main__":
    main()
