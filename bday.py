print("(putting a date like june 31st will work but should be treated as july 1st. you do not have to fill in all birthdays)")

name1 = input("Enter name for birthday 1: ")
day1 = int(input("Enter day: "))
month1 = int(input("Enter month: "))

if day1 > 31 or month1 > 12:
    print("invalid date")
else:
    print("Birthday 1:", name1)
    print(day1, month1, sep="/")

name2 = input("Enter name for birthday 2: ")
day2 = int(input("Enter day: "))
month2 = int(input("Enter month: "))

if day2 > 31 or month2 > 12:
    print("invalid date")
else:
    print("Birthday 2:", name2)
    print(day2, month2, sep="/")

name3 = input("Enter name for birthday 3: ")
day3 = int(input("Enter day: "))
month3 = int(input("Enter month: "))

if day3 > 31 or month3 > 12:
    print("invalid date")
else:
    print("Birthday 3:", name3)
    print(day3, month3, sep="/")

name4 = input("Enter name for birthday 4: ")
day4 = int(input("Enter day: "))
month4 = int(input("Enter month: "))

if day4 > 31 or month4 > 12:
    print("invalid date")
else:
    print("Birthday 4:", name4)
    print(day4, month4, sep="/")

name5 = input("Enter name for birthday 5: ")
day5 = int(input("Enter day: "))
month5 = int(input("Enter month: "))

if day5 > 31 or month5 > 12:
    print("invalid date")
else:
    print("Birthday 5:", name5)
    print(day5, month5, sep="/")

print("\nAll birthdays have been written down.")