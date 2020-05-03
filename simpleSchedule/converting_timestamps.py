import os
import json

def parse_timestamps(time_stamp_test):
    time_stamps = [i for i in time_stamp_test]
    return time_stamps

def time_stamp_return(day):
    schedule = []
    if os.path.isfile('schedule.txt'):
            with open('schedule.txt', 'r') as f:
                tempApps = f.read()
                converted = json.loads(tempApps)
                parse_timestamps(converted[day].keys())
                return parse_timestamps(converted[day].keys())

def main():
    day = input("Which day do you want to know about? : ")
    print(time_stamp_return(day))

if __name__ == '__main__':
    main()