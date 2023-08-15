from datetime import date, timedelta

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

delta = timedelta(days=1)

sunday_no = 0

while start_date <= end_date:
    # .day == 1 means the first of the month
    # .weekday() == 6 means Sunday
    if start_date.day == 1 and start_date.weekday() == 6:
        sunday_no += 1
    start_date += delta

print(sunday_no) # 171