1.from datetime import date

birth_year = int(input("Enter birth year (YYYY): "))
birth_month = int(input("Enter birth month (MM): "))
birth_day = int(input("Enter birth day (DD): "))

birth_date = date(birth_year, birth_month, birth_day)
today = date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12

print(f"Your age is {years} years, {months} months, and {days} days.")
2.from datetime import date

birth_year = int(input("Enter birth year (YYYY): "))
birth_month = int(input("Enter birth month (MM): "))
birth_day = int(input("Enter birth day (DD): "))

today = date.today()
next_birthday = date(today.year, birth_month, birth_day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birth_month, birth_day)

days_left = (next_birthday - today).days
print(f"Days until next birthday: {days_left}")
3.from datetime import datetime, timedelta

current = input("Enter current date & time (YYYY-MM-DD HH:MM): ")
hours = int(input("Meeting duration hours: "))
minutes = int(input("Meeting duration minutes: "))

start_time = datetime.strptime(current, "%Y-%m-%d %H:%M")
duration = timedelta(hours=hours, minutes=minutes)

end_time = start_time + duration
print("Meeting ends at:", end_time)
4.from datetime import datetime
import pytz

date_time = input("Enter date & time (YYYY-MM-DD HH:MM): ")
from_zone = input("Enter your timezone (e.g. Asia/Tashkent): ")
to_zone = input("Enter target timezone (e.g. Europe/London): ")

dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)

localized = from_tz.localize(dt)
converted = localized.astimezone(to_tz)

print("Converted time:", converted)
5.import time
from datetime import datetime

future = input("Enter future date & time (YYYY-MM-DD HH:MM:SS): ")
target = datetime.strptime(future, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = target - now

    if remaining.total_seconds() <= 0:
        print("Time reached!")
        break

    print("Time remaining:", remaining)
    time.sleep(1)
6.import re

email = input("Enter email address: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
7.number = input("Enter phone number (10 digits): ")

if len(number) == 10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatted number:", formatted)
else:
    print("Invalid phone number")
8.import re

password = input("Enter password: ")

if (len(password) >= 8 and
    re.search("[A-Z]", password) and
    re.search("[a-z]", password) and
    re.search("[0-9]", password)):
    print("Strong password")
else:
    print("Weak password")
9.text = input("Enter text: ")
word = input("Enter word to find: ")

words = text.lower().split()
count = words.count(word.lower())

print(f"The word '{word}' appears {count} times.")
10.import re

text = input("Enter text: ")

pattern = r'\b\d{4}-\d{2}-\d{2}\b'
dates = re.findall(pattern, text)

if dates:
    print("Dates found:")
    for d in dates:
        print(d)
else:
    print("No dates found.")
