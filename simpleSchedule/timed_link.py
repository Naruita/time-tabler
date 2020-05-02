import datetime
import webbrowser as webb
from time import sleep
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
op = webb.get('opera')

def link_open():
    op.open("https://m.teamlink.co/7706072174?p=83b0953304ad70075faa84c94f63a6fd")
    time.delay(20)
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
