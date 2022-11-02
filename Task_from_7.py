# 7 #############################################
# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.

num = int(input("Введите число : "))
mon = int(input("Введите месяц (1 - 12) : "))
ye = int(input("Введите год : "))


def date(day, month, year):
    if year >= 0:  # year should be >=0
        print("Year is correct")
        if 1 <= month <= 12:
            print("Month is correct")

            if 1 <= day <= 31:
                print("Day is correct")
    else:
        print("Error data")


date(num, mon, ye)
