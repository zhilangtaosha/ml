def main():

    input_data = input()
    backup_size, disk_size, price = map(int, input_data.split(" "))
    disk_num = 1
    total_size = 0

    if backup_size <= disk_size:
        print(price*disk_num)
    else:
        while True:
            disk_num += 1
            total_size = disk_size * disk_num
            if backup_size <= total_size:
                print(price*disk_num)
                break

if __name__ == '__main__':
    main()

"""
    while backup_size > total_size:
        disk_num += 1
        total_size = disk_size * disk_num
"""
