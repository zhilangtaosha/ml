

guess_me = 7

start = 1

while True:
    if start > guess_me:
        print("oops")
        break
    elif start < guess_me:
        print("too low")
    elif guess_me == start:
        print("found it!")
        break
    start += 1
