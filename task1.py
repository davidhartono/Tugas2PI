from datetime import datetime, timedelta

days = int(input("Enter a number of days: "))

future_date = datetime.now() + timedelta(days=days)

formatted_date = future_date.strftime("%A, %B %d, %Y")
print(formatted_date)
