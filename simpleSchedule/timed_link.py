import datetime
import webbrowser as webb
from time import sleep
from pynput.keyboard import Key, Controller
import time
import os
import json

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

keyboard = Controller()

def link_open():
    webb.open("https://m.teamlink.co/7706072174?p=83b0953304ad70075faa84c94f63a6fd")
    time.sleep(20)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

now = datetime.datetime.now()
print(now)
run_at = now + datetime.timedelta(seconds=5)
print(run_at)
delay = (run_at - now).total_seconds()
print(delay)

sleep(delay)
link_open()
