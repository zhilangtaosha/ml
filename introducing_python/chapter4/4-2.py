

guess_me = 7

start = 1

while start <= guess_me:
    if guess_me > start:
        print("too low")
    elif guess_me == start:
        print("found it!")
    start += 1
else:
    print("oops")
