import datetime
import webbrowser as webb
from time import sleep
import time
import os
import json
import deploy

# function to provide the current day the user is in.
def find_day():
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = week_days[datetime.date.today().weekday()]
    return day

# funtion to parse the file and provide the url for the particular timestamp.
def parse_file_link(course_urls):
    temp = course_urls.values()
    links = [j for i in temp for j in i]
    return links

# supposed to be the main part which reads the file and sends it to different functions.
def main():
    schedule = []

    if os.path.isfile('schedule.txt'):
        with open('schedule.txt', 'r') as f:
            tempApps = f.read()
            converted = json.loads(tempApps)
            days = converted.keys()
            schedule.append(converted.values())

    timestamp = '0900' # just need to get the timestamps now.

    temp_links = parse_file_link(converted[find_day()][timestamp])
    deploy.deploy_links(temp_links)

main()