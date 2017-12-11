#C023:クジの当選番号

def main():

    input_n_list = list(map(int,input().split(" ")))
    input_num = int(input())
    combine = []

    for _ in range(input_num):
        user_input_n_list = list(map(int,input().split(" ")))
        combine.append(user_input_n_list)

    count = 0
    for user_input in combine:
        for num in input_n_list:
            if num in user_input:
                count = count + 1

        print(count)
        count = 0

if __name__ == "__main__":
    main()
