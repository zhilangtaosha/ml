


number_things = ("Got %s" % number for number in range(10))
number_list = list(number_things)
print(number_list)

for thing in ("Got %s" % number for number in range(10)):
    print(thing)
