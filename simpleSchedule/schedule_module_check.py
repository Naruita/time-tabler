import schedule
import time
import datetime
import converting_timestamps as ct

def simpleExecute():
    print("This is working for now.")

def find_day():
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = week_days[datetime.date.today().weekday()]
    return day

schedule.every().find_day.at(ct.time_stamps).do(simpleExecute)

while True:
    schedule.run_pending()
    time.sleep(1)