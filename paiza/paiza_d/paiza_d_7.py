"""
D075:足りないカード
"""
def main():
    input_array = set([])
    true_array = {1, 2, 3, 4, 5}
    for i in range(4):
        input_num = int(input())
        input_array.add(input_num)

    ans = true_array-set(input_array)

    print(ans.pop())

if __name__ ==  '__main__':
    main()
