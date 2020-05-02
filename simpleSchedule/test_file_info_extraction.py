import os
import json
import datetime

week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
day = week_days[datetime.date.today().weekday()]


schedule = []
if os.path.isfile('schedule.txt'):
    with open('schedule.txt', 'r') as f:
        tempApps = f.read()
        converted = json.loads(tempApps)
        print("File info : ", converted)
        days = converted.keys()
        schedule.append(converted.values())

print(days)
print("\n\n", schedule)