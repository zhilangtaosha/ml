start_year = int(input('plz input start year '))
finish_year = int(input('plz input finish year '))

ary = []
for year in range(start_year, finish_year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                ary.append(str(year))
        else:
            ary.append(str(year))

print(','.join(ary))
print("there're %d leap years." % len(ary))
