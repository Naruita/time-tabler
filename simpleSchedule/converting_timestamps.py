import os
import json

def parse_timestamps(time_stamp_test):
    time_stamps = [i for i in time_stamp_test]
    return time_stamps


def convert_time(time_stamps):
    time_stamps_new = []
    for timestamp in time_stamps:
        time = ':'.join([timestamp[0:2], timestamp[2:4]])
        time_stamps_new.append(time)
    return time_stamps_new

today = "sunday"

schedule = []
if os.path.isfile('schedule.txt'):
        with open('schedule.txt', 'r') as f:
            tempApps = f.read()
            converted = json.loads(tempApps)
            time_stamps = converted["sunday"].keys()
            time_stamps = parse_timestamps(time_stamps)
            time_stamps = convert_time(time_stamps)
