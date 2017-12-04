def remaining(kg, percentage):
    return round(kg - kg * percentage / 100,4)

def main():
    kg, p1, p2 = list(map(int,input().split(" ")))

    print(remaining(remaining(kg,p1),p2))

if __name__ == "__main__":
    main()
