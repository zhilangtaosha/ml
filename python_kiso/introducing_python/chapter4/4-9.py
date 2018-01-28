

def get_odds():
#    yield (number for number in range(10) if number % 2 == 1)
#    yield (number for number in range(1,10,2))
    for number in range(1,10,2):
        yield number
#i=1

#for x in get_odds():
#    if i == 3:
#        print(x)
#    i += 1


for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The 3rd odd num is ", number)
        break
