

def test():
    assert leap_year(2016) == True
    assert leap_year(1900) == False
    assert leap_year(2000) == True
    assert leap_year(2017) == False

    assert num_days_in_month(1, 1900) == 31
    assert num_days_in_month(2, 2016) == 29
    assert num_days_in_month(2, 1900) == 28
    assert num_days_in_month(4, 2016) == 30

    assert num_days_in_year(2016) == 366
    assert num_days_in_year(1900) == 365

    assert is_sunday(7) == True
    assert is_sunday(32) == False
    
    assert num_days_from_1900(1, 1900) == 1
    assert num_days_from_1900(2, 1900) == 32

    assert is_sunday(num_days_from_1900(7, 2018)) == True



month_30 = (4, 6, 9, 11)
month_31 = (1, 3, 5, 7, 8, 10, 12)


def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def num_days_in_month(month, year):
    if month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    elif month in month_30:
        return 30
    elif month in month_31:
        return 31
    else:
        return f'something went wrong'


def num_days_in_year(year):
    if leap_year(year):
        return 366
    else:
        return 365


def is_sunday(n):
    if n % 7 == 0:
        return True
    else:
        return False


def num_days_from_1900(month, year):
    num_days_m = sum([num_days_in_month(m, year) for m in range(1, month)])
    # print(no_days_m)

    num_days_y = sum([num_days_in_year(y) for y in range(1900, year)])
    # print(no_days_y)

    num_days = num_days_m + num_days_y
    # print(num_days + 1)
    return num_days + 1



test()

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if is_sunday(num_days_from_1900(month, year)):
            count += 1


print(count) # == 171





# 1 Jan 1900 == Monday, 1900 not leap year
# 2 Jan 1900 == Tue



# a = is_sunday(day_num+1)
# print(a)

# class Date():

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def __repr__(self):
#         return f'Date({self.day}, {self.month}, {self.year})'

    
#     def __sub__(self, other):
#         return self.month - other.month


# x = Date(1, 1, 1900)
# print(x)
# y = Date(1, 2, 1900)
# print(y)
# print(y - x)



