def main():
    
    input_word_list = []

    for i in range(2):
        input_word = input()
        input_word_list.append(input_word)
        
    if input_word_list[0] in input_word_list[-1] :
        print("NG")
    else:
        print(input_word_list[1])

if __name__ == '__main__':
    main()
    