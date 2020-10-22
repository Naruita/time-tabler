#!usr/bin/python
# -*- coding: utf-8 -*-

# File managing
import json

# Time Stamp management
import datetime


""" This program is a testing program for the processing
 of the time difference between each of the stamps."""


def single_day_timestamp_difference(tesps):
    # TimE StamPS for tesps
    print(tesps)
    # datetime usage to check whether or not timestamp has passed.
    # Start from timestamp which is valid and not passed.


with open("schedule.txt", "r") as f:
    content = f.read()
    content = json.loads(content)
print(content)

""" The two following lines can be removed from this code as it 
exists in converting_timestamps.py, but for now, testing """
days = [i for i in content]
print(days)

for day in days:
    time_stamps = [i for i in content[day]]
    single_day_timestamp_difference(time_stamps)
