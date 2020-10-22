import datetime
import webbrowser as webb
from time import sleep
import time
import os
import json
import converting_timestamps as ct
import deploy
import schedule_module_check as smc

# function to provide the current day the user is in.
def find_day():
    week_days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    day = week_days[datetime.date.today().weekday()]
    return day


# funtion to parse the file and provide the url for the particular timestamp.
def parse_file_link(course_urls):
    temp = course_urls.values()
    links = [j for i in temp for j in i]
    return links


# supposed to be the main part which reads the file and sends it to different functions.
def execute():
    schedule = []

    if os.path.isfile("schedule.txt"):
        with open("schedule.txt", "r") as f:
            tempApps = f.read()
            converted = json.loads(tempApps)
            days = converted.keys()
            schedule.append(converted.values())

    timestamps = ct.time_stamp_return(
        find_day()
    )  # unformatted_timestamps -> 1900, timestamps -> 19:00
    for timestamp in timestamps:
        print(timestamp)
        temp_links = parse_file_link(converted[find_day()][timestamp])
        smc.scheduling(timestamp, temp_links)


if __name__ == "__main__":
    execute()
