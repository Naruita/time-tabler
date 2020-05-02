import os
import json
import datetime
import deploy

schedule = []

if os.path.isfile('schedule.txt'):
    with open('schedule.txt', 'r') as f:
        tempApps = f.read()
        converted = json.loads(tempApps)
        print("File info : ", converted)
        days = converted.keys()
        schedule.append(converted.values())

def find_day():
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = week_days[datetime.date.today().weekday()]
    return day

def link_open(course_urls):
    temp = course_urls.values()
    links = [j for i in temp for j in i]
    return links

timestamp = '0900' # Just need to get the timestamps parsed in.

temp_links = link_open(converted[find_day()][timestamp])
deploy.deploy_links(temp_links)
