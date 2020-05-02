import os
import re
import webbrowser as webb
import time
from pynput.keyboard import Key, Controller
import pickle

def deploy_links(team_links):
    keyboard = Controller()
    for team_link in team_links:
        if re.match(r"^https://m.teamlink.co", team_link):
            webb.open(team_link)
            time.sleep(20)
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:
            webb.open(team_link)
