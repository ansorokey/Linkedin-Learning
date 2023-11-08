import calendar

def count_days(y, m, d):
    # given a year, a month, and a day of the week
    # return the number of times that day of the wek appears that month
    cal = calendar.monthcalendar(y, m)
    count = 0
    for week in cal:
        if week[d] != 0:
            count += 1
    return count


print(count_days(2025, 12, 0))
