import json
'''
{
    "tuesday": {
        "08:50":
        [
            "https://m.teamlink.co/3456575612",
            "https://mail.google.com"
        ],
        "09:55":
        [
            "https://m.teamlink.co/1559268139",
            "https://www.github.com"
        ]
    }
}
'''
# the class creates a timetable for a single day
class day_timetable:
    def __init__(self, day):
        self.day = day
        self.time_table = {}
        self.timestamps = []

    # gets the timestamps, links, and appends them to the list/dictionary
    def get_info(self):
        self.in_time = input("Enter time in HH:MM format : ")
        self.timestamps.append(self.in_time)
        self.links = []
        print("Add links now. Type 'quit' to stop.")
        while True:
            temp_link = input("> ")
            if temp_link == 'quit':
                break
            else:
                self.links.append(temp_link)
        self.time_table[self.in_time] = self.links
        print(str(self.time_table)) # just prints to console for debugging. Can remove later.

    def day_return(self):
        return self.day

    def put_info(self):
        return self.time_table
    
    def timestamp_return(self):
        return self.timestamps

def make():
    week_timetable = {}

    while True:
        input_day_name = input("Enter the day : ").lower()
        current_day = day_timetable(input_day_name)
        while True:
            if input('Enter the upcoming class?(y/n) : ')[0] == 'y':
                current_day.get_info()
                week_timetable[current_day.day_return()] = current_day.put_info()
            else:
                break
        if input("Do you wish to enter entries for another day?(y/n) : ")[0] == 'n':
            break

    with open('../src/schedule.txt', 'w') as f:
        f.write(json.dumps(week_timetable, indent=4, sort_keys=True))

if __name__ == '__main__':
    make()