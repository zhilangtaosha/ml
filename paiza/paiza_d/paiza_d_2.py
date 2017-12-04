def main():

    input_scores = input()
    score_ilist = list(map(int,input_scores.split(" ")))

    ave_score = input()
    ave_score = int(ave_score)

    ave = sum(score_ilist) / len(score_ilist) 
    
    if ave >= ave_score: 
        print("pass")
    else:
        print("failure")

if __name__ == '__main__':
    main()